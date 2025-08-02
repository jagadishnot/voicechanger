import React, { useState, useRef, useEffect } from 'react';
import { ReactMic } from 'react-mic';
import { Mic, MicOff, Square, Play, Pause, RotateCcw, Volume2 } from 'lucide-react';

const AudioRecorder = ({ 
  onStop, 
  onStart, 
  isRecording, 
  setIsRecording,
  recordedAudio,
  setRecordedAudio 
}) => {
  const [audioLevel, setAudioLevel] = useState(0);
  const [recordingTime, setRecordingTime] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [volume, setVolume] = useState(1);
  const audioRef = useRef(null);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (isRecording) {
      intervalRef.current = setInterval(() => {
        setRecordingTime(prev => prev + 1);
      }, 1000);
    } else {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    }

    return () => {
      if (intervalRef.current) {
        clearInterval(intervalRef.current);
      }
    };
  }, [isRecording]);

  const startRecording = () => {
    setIsRecording(true);
    setRecordingTime(0);
    setRecordedAudio(null);
    if (onStart) onStart();
  };

  const stopRecording = () => {
    setIsRecording(false);
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  };

  const handleOnStop = (recordedData) => {
    setRecordedAudio(URL.createObjectURL(recordedData.blob));
    if (onStop) onStop(recordedData);
  };

  const resetRecording = () => {
    setRecordedAudio(null);
    setRecordingTime(0);
    setIsPlaying(false);
  };

  const togglePlayback = () => {
    if (audioRef.current) {
      if (isPlaying) {
        audioRef.current.pause();
      } else {
        audioRef.current.play();
      }
      setIsPlaying(!isPlaying);
    }
  };

  const handleVolumeChange = (e) => {
    const newVolume = parseFloat(e.target.value);
    setVolume(newVolume);
    if (audioRef.current) {
      audioRef.current.volume = newVolume;
    }
  };

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-celebrity border border-gray-200 dark:border-gray-700">
      <div className="text-center mb-6">
        <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
          Record Your Voice
        </h3>
        <p className="text-gray-600 dark:text-gray-400">
          {isRecording 
            ? 'Recording in progress...' 
            : recordedAudio 
              ? 'Recording complete! You can play it back or record again.'
              : 'Click the microphone to start recording your voice'
          }
        </p>
      </div>

      {/* Waveform Visualization */}
      <div className={`waveform-container mb-6 ${isRecording ? 'recording' : ''}`}>
        <ReactMic
          record={isRecording}
          className="sound-wave w-full h-32"
          onStop={handleOnStop}
          strokeColor={isRecording ? "#ef4444" : "#f97316"}
          backgroundColor="transparent"
          visualSetting="sinewave"
        />
        
        {/* Recording Status Overlay */}
        {isRecording && (
          <div className="absolute inset-0 flex items-center justify-center bg-error-50 dark:bg-error-900/20 rounded-xl">
            <div className="text-center">
              <div className="flex items-center justify-center mb-2">
                <div className="w-3 h-3 bg-error-500 rounded-full animate-pulse mr-2"></div>
                <span className="text-error-600 dark:text-error-400 font-medium">
                  REC {formatTime(recordingTime)}
                </span>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Recording Controls */}
      <div className="flex items-center justify-center gap-4 mb-6">
        {!isRecording ? (
          <button
            onClick={startRecording}
            className="audio-control-btn bg-primary-500 hover:bg-primary-600"
            disabled={false}
          >
            <Mic className="w-5 h-5" />
            Start Recording
          </button>
        ) : (
          <button
            onClick={stopRecording}
            className="audio-control-btn danger"
          >
            <Square className="w-5 h-5" />
            Stop Recording
          </button>
        )}

        {recordedAudio && !isRecording && (
          <>
            <button
              onClick={togglePlayback}
              className="audio-control-btn secondary"
            >
              {isPlaying ? (
                <>
                  <Pause className="w-5 h-5" />
                  Pause
                </>
              ) : (
                <>
                  <Play className="w-5 h-5" />
                  Play
                </>
              )}
            </button>

            <button
              onClick={resetRecording}
              className="audio-control-btn bg-gray-500 hover:bg-gray-600"
            >
              <RotateCcw className="w-5 h-5" />
              Reset
            </button>
          </>
        )}
      </div>

      {/* Audio Playback */}
      {recordedAudio && (
        <div className="bg-gray-50 dark:bg-gray-700 rounded-xl p-4">
          <div className="flex items-center gap-4 mb-3">
            <Volume2 className="w-5 h-5 text-gray-600 dark:text-gray-400" />
            <input
              type="range"
              min="0"
              max="1"
              step="0.1"
              value={volume}
              onChange={handleVolumeChange}
              className="flex-1 h-2 bg-gray-200 dark:bg-gray-600 rounded-lg appearance-none cursor-pointer"
            />
            <span className="text-sm text-gray-600 dark:text-gray-400 min-w-[3rem]">
              {Math.round(volume * 100)}%
            </span>
          </div>
          
          <audio
            ref={audioRef}
            src={recordedAudio}
            controls
            className="w-full"
            onPlay={() => setIsPlaying(true)}
            onPause={() => setIsPlaying(false)}
            onEnded={() => setIsPlaying(false)}
            volume={volume}
          />
        </div>
      )}

      {/* Recording Stats */}
      {(isRecording || recordedAudio) && (
        <div className="mt-4 flex justify-center">
          <div className="bg-gray-100 dark:bg-gray-700 rounded-lg px-4 py-2">
            <div className="flex items-center gap-4 text-sm">
              <div className="flex items-center gap-2">
                <div className={`w-2 h-2 rounded-full ${
                  isRecording ? 'bg-error-500 animate-pulse' : 'bg-success-500'
                }`}></div>
                <span className="text-gray-600 dark:text-gray-400">
                  {isRecording ? 'Recording' : 'Ready'}
                </span>
              </div>
              <div className="text-gray-600 dark:text-gray-400">
                Duration: {formatTime(recordingTime)}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AudioRecorder;