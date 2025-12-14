import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'https://stock-trend-api.onrender.com/api';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'multipart/form-data',
    },
});

export const stockPredictionAPI = {
    /**
     * Predict stock trend from image
     * @param {File} imageFile - Stock chart image file
     * @returns {Promise} - Prediction results
     */
    predictFromImage: async (imageFile) => {
        const formData = new FormData();
        formData.append('file', imageFile);

        const response = await api.post('/predict/image', formData);
        return response.data;
    },

    /**
     * Predict stock trend from numeric data (CSV)
     * @param {File} csvFile - CSV file with stock data
     * @returns {Promise} - Prediction results
     */
    predictFromNumeric: async (csvFile) => {
        const formData = new FormData();
        formData.append('file', csvFile);

        const response = await api.post('/predict/numeric', formData);
        return response.data;
    },

    /**
     * Health check
     * @returns {Promise} - API health status
     */
    healthCheck: async () => {
        const response = await api.get('/health');
        return response.data;
    },
};

export default api;
