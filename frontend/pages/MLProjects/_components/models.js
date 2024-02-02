"use client";

import { useEffect, useState } from 'react';
import axios from "axios";
// Define an interface for the model data

const Models = () => {
    // const [modelData, setModelData] = useState<ModelData | null>(null);
    const [modelData, setModelData] = useState(null);

    useEffect(() => {
        const fetchModelData = async () => {
            try {
                const response = await axios.get(`http://localhost:8080/models`);
                console.log("response data", response.data.models);
                setModelData(response.data.models);
                console.log("model data", modelData);
            } catch (error) {
                console.log("model data", modelData);
                console.error('Error fetching model data:', error);
            }
        };

        fetchModelData();
    }, []);

    return (
        <div>
            {modelData ? (
                <div>
                    <h2>Model: {modelData.model_name}</h2>
                    <p>AUC Score: {modelData.auc_score}</p>
                    <h3>Classification Report:</h3>
                    <pre>{JSON.stringify(modelData.classification_report, null, 2)}</pre>
                </div>
            ) : (
                <p>Loading...</p>
            )}

        </div>
    );
};

export default Models;
