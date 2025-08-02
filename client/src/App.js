import React, { useState, useEffect } from "react";
import axios from "axios";
import { Mic, Upload, Download, Share2, Search, Filter, Sparkles } from "lucide-react";

// Components
import CelebrityCard from "./components/CelebrityCard";
import ThemeToggle from "./components/ThemeToggle";
import AudioRecorder from "./components/AudioRecorder";
import FileUpload from "./components/FileUpload";

function App() {
  // State management
  const [celebrities, setCelebrities] = useState([]);
  const [filteredCelebrities, setFilteredCelebrities] = useState([]);
  const [selectedCelebrity, setSelectedCelebrity] = useState(null);
  const [activeCategory, setActiveCategory] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Audio states
  const [isRecording, setIsRecording] = useState(false);
  const [recordedAudio, setRecordedAudio] = useState(null);
  const [uploadedFile, setUploadedFile] = useState(null);
  const [convertedAudio, setConvertedAudio] = useState(null);
  const [isConverting, setIsConverting] = useState(false);
  const [conversionProgress, setConversionProgress] = useState(0);

  // UI states
  const [activeTab, setActiveTab] = useState("record"); // "record" or "upload"
  const [showCelebrityModal, setShowCelebrityModal] = useState(false);
  const [selectedCelebrityDetails, setSelectedCelebrityDetails] = useState(null);
  const [playingPreview, setPlayingPreview] = useState(null);

  // Categories
  const categories = [
    { id: "all", name: "All Stars", gradient: "bg-gradient-to-r from-primary-500 to-secondary-500" },
    { id: "bollywood", name: "Bollywood", gradient: "bollywood-gradient" },
    { id: "tollywood", name: "Tollywood", gradient: "tollywood-gradient" },
    { id: "kollywood", name: "Kollywood", gradient: "kollywood-gradient" },
    { id: "regional", name: "Regional", gradient: "regional-gradient" }
  ];

  // Fetch celebrities on component mount
  useEffect(() => {
    fetchCelebrities();
  }, []);

  // Filter celebrities based on category and search
  useEffect(() => {
    let filtered = celebrities;

    if (activeCategory !== "all") {
      filtered = filtered.filter(celebrity => celebrity.category === activeCategory);
    }

    if (searchQuery.trim()) {
      filtered = filtered.filter(celebrity =>
        celebrity.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        celebrity.voice_characteristics.some(char => 
          char.toLowerCase().includes(searchQuery.toLowerCase())
        )
      );
    }

    setFilteredCelebrities(filtered);
  }, [celebrities, activeCategory, searchQuery]);

  const fetchCelebrities = async () => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:5000/celebrities");
      
      setCelebrities(response.data.celebrities);
      setFilteredCelebrities(response.data.celebrities);
      
      // Set default selection to first celebrity
      if (response.data.celebrities.length > 0) {
        setSelectedCelebrity(response.data.celebrities[0]);
      }
    } catch (err) {
      setError("Failed to load celebrities. Please make sure the server is running.");
      console.error("Error fetching celebrities:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleRecordingStop = async (recordedData) => {
    if (!selectedCelebrity) {
      alert("Please select a celebrity first!");
      return;
    }

    try {
      setIsConverting(true);
      setConversionProgress(0);

      // Simulate progress
      const progressInterval = setInterval(() => {
        setConversionProgress(prev => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return 90;
          }
          return prev + 10;
        });
      }, 200);

      const formData = new FormData();
      formData.append("file", recordedData.blob);
      formData.append("celebrity", selectedCelebrity.id);

      const response = await axios.post("http://localhost:5000/convert", formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      clearInterval(progressInterval);
      setConversionProgress(100);

      setTimeout(() => {
        setConvertedAudio(`http://localhost:5000/results/${response.data.converted}`);
        setIsConverting(false);
        setConversionProgress(0);
      }, 500);

    } catch (err) {
      setIsConverting(false);
      setConversionProgress(0);
      setError("Voice conversion failed. Please try again.");
      console.error("Error converting voice:", err);
    }
  };

  const handleFileUpload = async (file) => {
    if (!file) {
      setUploadedFile(null);
      return;
    }

    setUploadedFile(file);

    if (!selectedCelebrity) {
      alert("Please select a celebrity first!");
      return;
    }

    try {
      setIsConverting(true);
      setConversionProgress(0);

      const progressInterval = setInterval(() => {
        setConversionProgress(prev => {
          if (prev >= 90) {
            clearInterval(progressInterval);
            return 90;
          }
          return prev + 10;
        });
      }, 200);

      const formData = new FormData();
      formData.append("file", file);
      formData.append("celebrity", selectedCelebrity.id);

      const response = await axios.post("http://localhost:5000/convert", formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      clearInterval(progressInterval);
      setConversionProgress(100);

      setTimeout(() => {
        setConvertedAudio(`http://localhost:5000/results/${response.data.converted}`);
        setIsConverting(false);
        setConversionProgress(0);
      }, 500);

    } catch (err) {
      setIsConverting(false);
      setConversionProgress(0);
      setError("Voice conversion failed. Please try again.");
      console.error("Error converting voice:", err);
    }
  };

  const handleCelebritySelect = (celebrity) => {
    setSelectedCelebrity(celebrity);
    setConvertedAudio(null); // Reset converted audio when changing celebrity
  };

  const handlePreviewVoice = async (celebrityId) => {
    try {
      // Stop any currently playing preview
      if (playingPreview) {
        setPlayingPreview(null);
        return;
      }

      setPlayingPreview(celebrityId);
      
      // Find the celebrity to get their voice sample path
      const celebrity = celebrities.find(c => c.id === celebrityId);
      if (!celebrity || !celebrity.voice_sample) {
        console.error("No voice sample found for celebrity:", celebrityId);
        setPlayingPreview(null);
        return;
      }

      // Create audio element and play the sample
      const audio = new Audio(`http://localhost:5000${celebrity.voice_sample}`);
      
      audio.onloadeddata = () => {
        audio.play().catch(err => {
          console.error("Error playing audio:", err);
          setPlayingPreview(null);
        });
      };

      audio.onended = () => {
        setPlayingPreview(null);
      };

      audio.onerror = (err) => {
        console.error("Error loading audio:", err);
        setPlayingPreview(null);
      };

    } catch (err) {
      console.error("Error playing preview:", err);
      setPlayingPreview(null);
    }
  };

  const handleShowDetails = (celebrity) => {
    setSelectedCelebrityDetails(celebrity);
    setShowCelebrityModal(true);
  };

  const downloadAudio = () => {
    if (convertedAudio) {
      const link = document.createElement('a');
      link.href = convertedAudio;
      link.download = `${selectedCelebrity.name}_voice_conversion.wav`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  };

  const shareAudio = async () => {
    if (navigator.share && convertedAudio) {
      try {
        await navigator.share({
          title: `Voice converted to ${selectedCelebrity.name}`,
          text: `Check out my voice converted to sound like ${selectedCelebrity.name}!`,
          url: convertedAudio
        });
      } catch (err) {
        console.error('Error sharing:', err);
      }
    } else {
      // Fallback: copy link to clipboard
      navigator.clipboard.writeText(convertedAudio);
      alert('Audio link copied to clipboard!');
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="loading-spinner w-12 h-12 mx-auto mb-4"></div>
          <p className="text-gray-600 dark:text-gray-400">Loading celebrities...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center max-w-md mx-auto p-6">
          <div className="text-error-500 text-6xl mb-4">⚠️</div>
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
            Something went wrong
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mb-4">{error}</p>
          <button
            onClick={fetchCelebrities}
            className="audio-control-btn"
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 shadow-lg border-b border-gray-200 dark:border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-gradient-to-r from-primary-500 to-secondary-500 rounded-xl">
                <Sparkles className="w-8 h-8 text-white" />
              </div>
              <div>
                <h1 className="text-2xl font-bold gradient-text">
                  Celebrity Voice Changer
                </h1>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  Transform your voice into Indian cinema stars
                </p>
              </div>
            </div>
            <ThemeToggle />
          </div>
        </div>
      </header>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Category Filter */}
        <div className="mb-8">
          <div className="flex flex-wrap gap-3 mb-4">
            {categories.map((category) => (
              <button
                key={category.id}
                onClick={() => setActiveCategory(category.id)}
                className={`category-tab ${activeCategory === category.id ? 'active' : ''}`}
              >
                {category.name}
              </button>
            ))}
          </div>

          {/* Search Bar */}
          <div className="relative max-w-md">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400" />
            <input
              type="text"
              placeholder="Search celebrities..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-10 pr-4 py-3 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-xl focus:ring-2 focus:ring-primary-500 focus:border-transparent"
            />
          </div>
        </div>

        {/* Celebrity Selection */}
        <div className="mb-8">
          <h2 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
            Choose Your Celebrity Voice ({filteredCelebrities.length})
          </h2>
          <div className="celebrity-grid">
            {filteredCelebrities.map((celebrity) => (
              <CelebrityCard
                key={celebrity.id}
                celebrity={celebrity}
                isSelected={selectedCelebrity?.id === celebrity.id}
                onSelect={handleCelebritySelect}
                onPreview={handlePreviewVoice}
                onShowDetails={handleShowDetails}
                isPlaying={playingPreview === celebrity.id}
              />
            ))}
          </div>
        </div>

        {/* Audio Input Section */}
        <div className="grid lg:grid-cols-2 gap-8 mb-8">
          {/* Input Method Tabs */}
          <div>
            <div className="flex gap-2 mb-6">
              <button
                onClick={() => setActiveTab("record")}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                  activeTab === "record"
                    ? "bg-primary-500 text-white"
                    : "bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300"
                }`}
              >
                <Mic className="w-4 h-4" />
                Record Voice
              </button>
              <button
                onClick={() => setActiveTab("upload")}
                className={`flex items-center gap-2 px-4 py-2 rounded-lg font-medium transition-colors ${
                  activeTab === "upload"
                    ? "bg-primary-500 text-white"
                    : "bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300"
                }`}
              >
                <Upload className="w-4 h-4" />
                Upload File
              </button>
            </div>

            {activeTab === "record" ? (
              <AudioRecorder
                onStop={handleRecordingStop}
                isRecording={isRecording}
                setIsRecording={setIsRecording}
                recordedAudio={recordedAudio}
                setRecordedAudio={setRecordedAudio}
              />
            ) : (
              <FileUpload
                onFileSelect={handleFileUpload}
              />
            )}
          </div>

          {/* Output Section */}
          <div>
            <div className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-celebrity border border-gray-200 dark:border-gray-700">
              <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-4">
                {selectedCelebrity ? `${selectedCelebrity.name}'s Voice` : "Select a Celebrity"}
              </h3>

              {isConverting ? (
                <div className="text-center py-8">
                  <div className="loading-spinner w-12 h-12 mx-auto mb-4"></div>
                  <p className="text-gray-600 dark:text-gray-400 mb-2">
                    Converting your voice...
                  </p>
                  <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                    <div
                      className="bg-primary-500 h-2 rounded-full transition-all duration-300"
                      style={{ width: `${conversionProgress}%` }}
                    ></div>
                  </div>
                  <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
                    {conversionProgress}% complete
                  </p>
                </div>
              ) : convertedAudio ? (
                <div>
                  <div className="bg-gray-50 dark:bg-gray-700 rounded-xl p-4 mb-4">
                    <audio controls src={convertedAudio} className="w-full" />
                  </div>
                  
                  <div className="flex gap-3">
                    <button
                      onClick={downloadAudio}
                      className="audio-control-btn secondary flex-1"
                    >
                      <Download className="w-4 h-4" />
                      Download
                    </button>
                    <button
                      onClick={shareAudio}
                      className="audio-control-btn bg-green-500 hover:bg-green-600 flex-1"
                    >
                      <Share2 className="w-4 h-4" />
                      Share
                    </button>
                  </div>
                </div>
              ) : (
                <div className="text-center py-8">
                  <div className="w-16 h-16 mx-auto mb-4 bg-gray-200 dark:bg-gray-700 rounded-full flex items-center justify-center">
                    {selectedCelebrity ? (
                      <span className="text-2xl">🎤</span>
                    ) : (
                      <span className="text-2xl">⭐</span>
                    )}
                  </div>
                  <p className="text-gray-600 dark:text-gray-400">
                    {selectedCelebrity
                      ? `Record or upload audio to convert to ${selectedCelebrity.name}'s voice`
                      : "Select a celebrity to get started"
                    }
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </div>

      {/* Celebrity Details Modal */}
      {showCelebrityModal && selectedCelebrityDetails && (
        <div className="modal-backdrop" onClick={() => setShowCelebrityModal(false)}>
          <div className="celebrity-modal" onClick={(e) => e.stopPropagation()}>
            <div className="p-6">
              <div className="flex items-start gap-4 mb-4">
                <img
                  src={selectedCelebrityDetails.image || `/images/celebrities/${selectedCelebrityDetails.id}.jpg`}
                  alt={selectedCelebrityDetails.name}
                  className="w-20 h-20 rounded-xl object-cover"
                  onError={(e) => {
                    e.target.src = `data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="80" height="80" viewBox="0 0 80 80"><rect width="80" height="80" fill="%23f3f4f6"/><text x="40" y="45" text-anchor="middle" font-size="24" fill="%236b7280">${selectedCelebrityDetails.name.charAt(0)}</text></svg>`;
                  }}
                />
                <div className="flex-1">
                  <h3 className="text-2xl font-bold text-gray-900 dark:text-white">
                    {selectedCelebrityDetails.name}
                  </h3>
                  <p className="text-primary-600 dark:text-primary-400 font-medium">
                    {selectedCelebrityDetails.category.charAt(0).toUpperCase() + selectedCelebrityDetails.category.slice(1)} Star
                  </p>
                  <p className="text-gray-600 dark:text-gray-400 text-sm">
                    Debut: {selectedCelebrityDetails.debut_year} • Popularity: {selectedCelebrityDetails.popularity}/100
                  </p>
                </div>
                <button
                  onClick={() => setShowCelebrityModal(false)}
                  className="p-2 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
                >
                  ✕
                </button>
              </div>
              
              <p className="text-gray-700 dark:text-gray-300 mb-4">
                {selectedCelebrityDetails.bio}
              </p>
              
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Voice Characteristics</h4>
                <div className="flex flex-wrap gap-2">
                  {selectedCelebrityDetails.voice_characteristics.map((char, index) => (
                    <span key={index} className="px-3 py-1 bg-primary-100 dark:bg-primary-900/30 text-primary-700 dark:text-primary-300 rounded-full text-sm">
                      {char}
                    </span>
                  ))}
                </div>
              </div>
              
              <div className="mb-4">
                <h4 className="font-semibold text-gray-900 dark:text-white mb-2">Notable Films</h4>
                <div className="flex flex-wrap gap-2">
                  {selectedCelebrityDetails.notable_films.map((film, index) => (
                    <span key={index} className="px-3 py-1 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-300 rounded-full text-sm">
                      {film}
                    </span>
                  ))}
                </div>
              </div>
              
              <div className="flex gap-3">
                <button
                  onClick={() => {
                    handleCelebritySelect(selectedCelebrityDetails);
                    setShowCelebrityModal(false);
                  }}
                  className="audio-control-btn flex-1"
                >
                  Select This Voice
                </button>
                <button
                  onClick={() => handlePreviewVoice(selectedCelebrityDetails.id)}
                  className="audio-control-btn secondary"
                >
                  Preview Voice
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
