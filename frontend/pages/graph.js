
"use client";

import { useEffect, useState } from 'react';
import axios from 'axios';

const Graph = () => {
    const [imageUrl, setImageUrl] = useState('');

    useEffect(() => {
        const fetchImage = async () => {
            try {
                const response = await axios.get('http://localhost:8080/first_image', { responseType: 'blob' });
                const imageUrl = URL.createObjectURL(response.data);
                setImageUrl(imageUrl);
            } catch (error) {
                console.error('Error fetching image:', error);
            }
        };

        fetchImage();
    }, []);

    return (
        <div>
            {imageUrl ? (
                // <Image />
                <img src={imageUrl} alt="Generated Image" />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default Graph;
