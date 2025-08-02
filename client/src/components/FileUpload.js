import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import { Upload, File, X, CheckCircle, AlertCircle } from 'lucide-react';

const FileUpload = ({ onFileSelect, acceptedFiles, maxSize = 10485760 }) => { // 10MB default
  const [uploadedFile, setUploadedFile] = useState(null);
  const [error, setError] = useState(null);

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    setError(null);
    
    if (rejectedFiles.length > 0) {
      const rejection = rejectedFiles[0];
      if (rejection.errors[0].code === 'file-too-large') {
        setError(`File is too large. Maximum size is ${Math.round(maxSize / 1024 / 1024)}MB`);
      } else if (rejection.errors[0].code === 'file-invalid-type') {
        setError('Invalid file type. Please upload an audio file (MP3, WAV, M4A, etc.)');
      } else {
        setError('File upload failed. Please try again.');
      }
      return;
    }

    if (acceptedFiles.length > 0) {
      const file = acceptedFiles[0];
      setUploadedFile(file);
      if (onFileSelect) {
        onFileSelect(file);
      }
    }
  }, [onFileSelect, maxSize]);

  const {
    getRootProps,
    getInputProps,
    isDragActive,
    isDragAccept,
    isDragReject
  } = useDropzone({
    onDrop,
    accept: {
      'audio/*': ['.mp3', '.wav', '.m4a', '.aac', '.ogg', '.flac']
    },
    maxSize,
    multiple: false
  });

  const removeFile = () => {
    setUploadedFile(null);
    setError(null);
    if (onFileSelect) {
      onFileSelect(null);
    }
  };

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  const getDropzoneClassName = () => {
    let className = 'dropzone transition-all duration-200 ';
    
    if (isDragActive) {
      className += 'active ';
    }
    
    if (isDragAccept) {
      className += 'border-success-500 bg-success-50 dark:bg-success-900/20 ';
    } else if (isDragReject) {
      className += 'border-error-500 bg-error-50 dark:bg-error-900/20 ';
    } else if (isDragActive) {
      className += 'border-primary-500 bg-primary-50 dark:bg-primary-900/20 ';
    }
    
    return className;
  };

  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl p-6 shadow-celebrity border border-gray-200 dark:border-gray-700">
      <div className="text-center mb-6">
        <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
          Upload Audio File
        </h3>
        <p className="text-gray-600 dark:text-gray-400">
          Drag and drop an audio file or click to browse
        </p>
      </div>

      {!uploadedFile ? (
        <div {...getRootProps()} className={getDropzoneClassName()}>
          <input {...getInputProps()} />
          
          <div className="text-center py-8">
            <Upload className={`w-12 h-12 mx-auto mb-4 ${
              isDragActive 
                ? 'text-primary-500' 
                : 'text-gray-400 dark:text-gray-500'
            }`} />
            
            {isDragActive ? (
              <p className="text-primary-600 dark:text-primary-400 font-medium">
                {isDragAccept 
                  ? 'Drop the audio file here...' 
                  : 'This file type is not supported'
                }
              </p>
            ) : (
              <div>
                <p className="text-gray-600 dark:text-gray-400 mb-2">
                  <span className="font-medium text-primary-600 dark:text-primary-400">
                    Click to upload
                  </span> or drag and drop
                </p>
                <p className="text-sm text-gray-500 dark:text-gray-500">
                  MP3, WAV, M4A, AAC, OGG, FLAC (max {Math.round(maxSize / 1024 / 1024)}MB)
                </p>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div className="bg-gray-50 dark:bg-gray-700 rounded-xl p-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="p-2 bg-success-100 dark:bg-success-900/30 rounded-lg">
                <File className="w-6 h-6 text-success-600 dark:text-success-400" />
              </div>
              
              <div>
                <p className="font-medium text-gray-900 dark:text-white truncate max-w-xs">
                  {uploadedFile.name}
                </p>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  {formatFileSize(uploadedFile.size)}
                </p>
              </div>
            </div>
            
            <div className="flex items-center gap-2">
              <CheckCircle className="w-5 h-5 text-success-500" />
              <button
                onClick={removeFile}
                className="p-1 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-full transition-colors duration-200"
                title="Remove file"
              >
                <X className="w-4 h-4 text-gray-500 dark:text-gray-400" />
              </button>
            </div>
          </div>
          
          {/* Audio Preview */}
          <div className="mt-4">
            <audio
              controls
              src={URL.createObjectURL(uploadedFile)}
              className="w-full"
            />
          </div>
        </div>
      )}

      {error && (
        <div className="mt-4 p-4 bg-error-50 dark:bg-error-900/20 border border-error-200 dark:border-error-800 rounded-xl">
          <div className="flex items-center gap-2">
            <AlertCircle className="w-5 h-5 text-error-500" />
            <p className="text-error-700 dark:text-error-400 font-medium">
              {error}
            </p>
          </div>
        </div>
      )}

      {/* Upload Tips */}
      <div className="mt-6 bg-blue-50 dark:bg-blue-900/20 rounded-xl p-4">
        <h4 className="font-medium text-blue-900 dark:text-blue-100 mb-2">
          Tips for best results:
        </h4>
        <ul className="text-sm text-blue-700 dark:text-blue-300 space-y-1">
          <li>• Use clear, high-quality audio recordings</li>
          <li>• Minimize background noise</li>
          <li>• Keep recordings between 5-30 seconds for optimal conversion</li>
          <li>• Speak clearly and at a normal pace</li>
        </ul>
      </div>
    </div>
  );
};

export default FileUpload;