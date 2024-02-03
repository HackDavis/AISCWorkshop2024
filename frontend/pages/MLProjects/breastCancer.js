import Head from 'next/head';
import styles from '../../styles/breastCancer.module.scss';
import Image from 'next/image';
import Graph from './_components/graph';
import Models from './_components/models';
import Analysis from './_components/analysis';
import { useState } from 'react';

export default function MLProjects() {

  const mlModels = ['logistic_regression', 'k_nearest_neighbors', 'support_vector_machine', 'decision_tree',
    'random_forest', 'gradient_boosting', 'naive_bayes', 'neural_network', 'ada_boost', 'xg_boost']

  const [checkedModels, setCheckedModels] = useState([]);
  const [chosenModels, setChosenModels] = useState([]);

  const checklistHandler = (modelName) => {
    if (checkedModels.includes(modelName)) {
      setCheckedModels((models) => models.filter((i) => i !== modelName));
    } else {
      setCheckedModels((models) => [...models, modelName]);
    }
  }

  const buttonHandler = (allModels) => {
    setChosenModels(allModels);
    setCheckedModels([]);

    console.log("CHOSEN MODELS", chosenModels);
    console.log("CHECKED MODELS", checkedModels);
  }



  return (
    <div className={styles.container}>
      <div className={styles.container_inside}>
        <div className={styles.container_inside_window}>
          <div className={styles.container_inside_window_Card} style={{ backgroundColor: "" }}>
            <h1>Machine Learning Models</h1>
            <div className={styles.container_checklist_container}>
              {mlModels.map((model, index) => {
                return (
                  <div className={styles.container_checklist_container_inside} key={index} >
                    <input id={model} type='checkbox' onChange={() => checklistHandler(model)} />
                    <label>{model}</label>
                  </div>)
              })}

            </div>
            <button className={styles.container_checklist_container_button} onClick={() => buttonHandler(checkedModels)}>Submit</button>
          </div>
          <div className={styles.container_inside_window_Card}>
            <p>Model Details:</p>
            <Models props={chosenModels} />
          </div>
          <div className={styles.container_inside_window_Card}>
            <p>ROC curve: (False positives vs True positives ratio)</p>
            <Graph />
          </div>
          <div className={styles.container_inside_window_Card}>
            <p> Scatter plot for feature analysis (pre-processing) </p>
            <Analysis />
          </div>
        </div>
        <div className={styles.container_inside_animals}>
          <Image src="/MLProjects/cow.svg" alt="cow" width={100} height={100} />
          <Image src="/MLProjects/bunny.svg" alt="bunny" width={100} height={100} />
          <Image src="/MLProjects/duck.svg" alt="duck" width={100} height={100} />
          <Image src="/MLProjects/frog.svg" alt="frog" width={100} height={100} />
        </div>
      </div>
    </div>
  );
}
