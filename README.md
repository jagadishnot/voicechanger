# Celebrity Voice Changer - Enhanced Edition

Transform your voice into iconic Indian cinema stars with our advanced AI-powered voice conversion application. Experience the magic of Bollywood, Tollywood, Kollywood, and regional cinema voices with a modern, responsive interface.

## 🌟 Features

### 🎭 Celebrity Voice Collection
- **24+ Indian Cinema Stars** across different film industries
- **Bollywood Legends**: Amitabh Bachchan, Shah Rukh Khan, Aamir Khan, Salman Khan, Deepika Padukone, Priyanka Chopra, Hrithik Roshan, Akshay Kumar
- **Tollywood Stars**: Prabhas, Mahesh Babu, Jr. NTR, Ram Charan, Samantha Ruth Prabhu, Rashmika Mandanna
- **Kollywood Icons**: Rajinikanth, Vijay, Kamal Haasan, Suriya, Dhanush, Nayanthara
- **Regional Stars**: Yash, Dulquer Salmaan, Allu Arjun, Fahadh Faasil

### 🎨 Modern UI/UX
- **Dark/Light Theme** with Indian cinema-inspired color palettes
- **Responsive Design** optimized for mobile, tablet, and desktop
- **Interactive Celebrity Cards** with hover effects and animations
- **Category Filtering** by film industry (Bollywood/Tollywood/Kollywood/Regional)
- **Search Functionality** to find celebrities by name or voice characteristics
- **Celebrity Profile Modals** with detailed information and filmography

### 🎤 Advanced Audio Features
- **Dual Input Methods**: Record voice or upload audio files
- **Real-time Waveform Visualization** during recording
- **Audio Format Support**: MP3, WAV, M4A, AAC, OGG, FLAC
- **Drag & Drop File Upload** with validation and preview
- **Enhanced Playback Controls** with volume adjustment
- **Voice Comparison** between original and converted audio
- **Download & Share** converted audio files

### 🔧 Technical Features
- **Loading States** and progress indicators
- **Error Handling** with user-friendly messages
- **Voice Preview** functionality for celebrity samples
- **Batch Conversion** support (API ready)
- **Conversion History** tracking
- **PWA Ready** for mobile installation

## 🚀 Quick Start

### Prerequisites
- Node.js (v14 or higher)
- Python 3.8+
- npm or yarn

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd voice-swapper-app
   ```

2. **Install Frontend Dependencies**
   ```bash
   cd client
   npm install --legacy-peer-deps
   ```

3. **Install Backend Dependencies**
   ```bash
   cd ../server
   pip install fastapi uvicorn python-multipart
   ```

4. **Start the Backend Server**
   ```bash
   python main.py
   ```
   Server will run on `http://localhost:5000`

5. **Start the Frontend Application**
   ```bash
   cd ../client
   npm start
   ```
   Application will open on `http://localhost:3000`

## 📱 Usage Guide

### 1. Select a Celebrity Voice
- Browse through different categories (Bollywood, Tollywood, Kollywood, Regional)
- Use the search bar to find specific celebrities
- Click on celebrity cards to select them
- View detailed profiles by clicking the info button

### 2. Record or Upload Audio
- **Record**: Click "Record Voice" tab and use the microphone
- **Upload**: Click "Upload File" tab and drag/drop or browse for audio files
- Supported formats: MP3, WAV, M4A, AAC, OGG, FLAC (max 10MB)

### 3. Convert Your Voice
- Conversion starts automatically after recording/uploading
- Watch the progress indicator during conversion
- Preview the converted audio with playback controls

### 4. Download & Share
- Download converted audio in WAV format
- Share directly using the native share API
- Compare original vs converted audio side-by-side

## 🎨 Design System

### Color Palette
- **Primary**: Orange gradient (#f97316 to #c2410c) - Inspired by Indian cinema
- **Secondary**: Blue gradient (#0ea5e9 to #0369a1) - Tollywood theme
- **Accent**: Purple gradient (#d946ef to #a21caf) - Kollywood theme
- **Success**: Green (#22c55e) - Regional cinema theme

### Typography
- **Primary Font**: Poppins (Display and headings)
- **Secondary Font**: Inter (Body text)
- **Responsive Text Sizes** for optimal readability

### Components
- **Celebrity Cards**: Hover effects, selection states, category badges
- **Audio Controls**: Modern button design with icons
- **Theme Toggle**: Smooth dark/light mode transition
- **Modal Dialogs**: Celebrity details with backdrop blur

## 🔧 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### Get All Celebrities
```http
GET /celebrities
```
Query Parameters:
- `category` (optional): Filter by category
- `search` (optional): Search by name or characteristics
- `limit` (optional): Limit number of results

#### Get Categories
```http
GET /categories
```

#### Get Celebrity Details
```http
GET /celebrity/{celebrity_id}
```

#### Convert Voice
```http
POST /convert
```
Form Data:
- `file`: Audio file
- `celebrity`: Celebrity ID

#### Get Voice Sample
```http
GET /preview/{celebrity_id}
```

#### Get Converted Audio
```http
GET /results/{filename}
```

## 🏗️ Architecture

### Frontend (React)
```
src/
├── components/
│   ├── CelebrityCard.js      # Celebrity selection cards
│   ├── ThemeToggle.js        # Dark/light mode toggle
│   ├── AudioRecorder.js      # Voice recording interface
│   └── FileUpload.js         # File upload with drag & drop
├── App.js                    # Main application component
├── index.css                 # Tailwind CSS with custom styles
└── index.js                  # Application entry point
```

### Backend (FastAPI)
```
server/
├── main.py                   # FastAPI application with all endpoints
├── celebrities.py            # Celebrity database and utilities
├── uploads/                  # Uploaded audio files
├── results/                  # Converted audio files
└── static/                   # Static assets (images, samples)
```

## 🎯 Celebrity Database Structure

Each celebrity entry contains:
```json
{
  "id": "celebrity_id",
  "name": "Celebrity Name",
  "category": "bollywood|tollywood|kollywood|regional",
  "image": "/images/celebrities/celebrity.jpg",
  "bio": "Detailed biography...",
  "voice_sample": "/samples/celebrity_sample.wav",
  "languages": ["hindi", "english"],
  "popularity": 95,
  "debut_year": 1990,
  "notable_films": ["Film 1", "Film 2"],
  "voice_characteristics": ["deep", "authoritative"]
}
```

## 🔮 Future Enhancements

### Planned Features
- **Real AI Voice Conversion** using RVC or SoVITS models
- **Voice Training** for custom celebrity voices
- **Multi-language Support** with automatic detection
- **Voice Effects** and audio filters
- **User Accounts** with conversion history
- **Social Features** for sharing and rating
- **Mobile App** with native recording
- **API Rate Limiting** and authentication

### Technical Improvements
- **WebRTC** for real-time voice processing
- **WebAssembly** for client-side audio processing
- **CDN Integration** for faster asset delivery
- **Database Integration** (PostgreSQL/MongoDB)
- **Docker Containerization** for easy deployment
- **CI/CD Pipeline** with automated testing

## 🐛 Troubleshooting

### Common Issues

1. **Dependencies Installation Failed**
   ```bash
   npm install --legacy-peer-deps --force
   ```

2. **Server Not Starting**
   - Check if port 5000 is available
   - Install missing Python dependencies
   - Verify Python version (3.8+)

3. **Audio Recording Not Working**
   - Grant microphone permissions in browser
   - Use HTTPS for production deployment
   - Check browser compatibility

4. **File Upload Issues**
   - Verify file format is supported
   - Check file size (max 10MB)
   - Ensure server has write permissions

### Browser Compatibility
- **Chrome**: Full support
- **Firefox**: Full support
- **Safari**: Limited WebRTC support
- **Edge**: Full support
- **Mobile Browsers**: Basic functionality

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the API documentation

## 🙏 Acknowledgments

- Indian cinema industry for inspiration
- React and FastAPI communities
- Tailwind CSS for the design system
- All the amazing celebrities featured in the app

---

**Made with ❤️ for Indian Cinema Fans**

Transform your voice, embrace the magic! 🎭✨