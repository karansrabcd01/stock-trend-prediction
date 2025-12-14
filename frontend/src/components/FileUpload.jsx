import React, { useState, useRef } from 'react';
import { Upload, Image, FileText, X } from 'lucide-react';
import './FileUpload.css';

const FileUpload = ({ onFileSelect, predictionType, isLoading }) => {
    const [dragActive, setDragActive] = useState(false);
    const [preview, setPreview] = useState(null);
    const [fileName, setFileName] = useState('');
    const fileInputRef = useRef(null);

    const acceptedTypes = predictionType === 'image'
        ? 'image/jpeg,image/png,image/jpg,image/bmp'
        : '.csv,text/csv';

    const handleDrag = (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (e.type === "dragenter" || e.type === "dragover") {
            setDragActive(true);
        } else if (e.type === "dragleave") {
            setDragActive(false);
        }
    };

    const handleDrop = (e) => {
        e.preventDefault();
        e.stopPropagation();
        setDragActive(false);

        if (e.dataTransfer.files && e.dataTransfer.files[0]) {
            handleFile(e.dataTransfer.files[0]);
        }
    };

    const handleChange = (e) => {
        e.preventDefault();
        if (e.target.files && e.target.files[0]) {
            handleFile(e.target.files[0]);
        }
    };

    const handleFile = (file) => {
        setFileName(file.name);

        if (predictionType === 'image') {
            const reader = new FileReader();
            reader.onloadend = () => {
                setPreview(reader.result);
            };
            reader.readAsDataURL(file);
        }

        onFileSelect(file);
    };

    const clearFile = () => {
        setFileName('');
        setPreview(null);
        onFileSelect(null);
        if (fileInputRef.current) {
            fileInputRef.current.value = '';
        }
    };

    const onButtonClick = () => {
        fileInputRef.current?.click();
    };

    return (
        <div className="file-upload-container">
            <input
                ref={fileInputRef}
                type="file"
                accept={acceptedTypes}
                onChange={handleChange}
                style={{ display: 'none' }}
                disabled={isLoading}
            />

            {!fileName ? (
                <div
                    className={`upload-area ${dragActive ? 'drag-active' : ''}`}
                    onDragEnter={handleDrag}
                    onDragLeave={handleDrag}
                    onDragOver={handleDrag}
                    onDrop={handleDrop}
                    onClick={onButtonClick}
                >
                    <div className="upload-icon">
                        {predictionType === 'image' ? (
                            <Image size={48} />
                        ) : (
                            <FileText size={48} />
                        )}
                    </div>
                    <h3>
                        {predictionType === 'image'
                            ? 'Upload Stock Chart Image'
                            : 'Upload Stock Data CSV'}
                    </h3>
                    <p>Drag and drop or click to browse</p>
                    <p className="upload-hint">
                        {predictionType === 'image'
                            ? 'Supported: JPG, PNG, BMP (Max 10MB)'
                            : 'Required columns: close, high, low, volume (Max 5MB)'}
                    </p>
                </div>
            ) : (
                <div className="file-preview">
                    {preview && (
                        <div className="image-preview">
                            <img src={preview} alt="Preview" />
                        </div>
                    )}
                    <div className="file-info">
                        <div className="file-name">
                            {predictionType === 'image' ? <Image size={20} /> : <FileText size={20} />}
                            <span>{fileName}</span>
                        </div>
                        {!isLoading && (
                            <button className="clear-btn" onClick={clearFile}>
                                <X size={20} />
                            </button>
                        )}
                    </div>
                </div>
            )}
        </div>
    );
};

export default FileUpload;
