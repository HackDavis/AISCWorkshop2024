import Head from 'next/head';
import styles from '../styles/Home.module.scss';
import Image from 'next/image';

export default function Home() {
  return (
    <div className={styles.container}>
      <div className={styles.container_inside}>
        <div className={styles.container_inside_window}>
        <div className={styles.container_inside_window_Card} />
        <div className={styles.container_inside_window_Card} />
        <div className={styles.container_inside_window_Card} />
        <div className={styles.container_inside_window_Card} />
        </div>
        <div className={styles.container_inside_animals}>
          <Image src="/index/cow.svg" alt="cow" width={100} height={100} />
          <Image src="/index/bunny.svg" alt="bunny" width={100} height={100} />
          <Image src="/index/duck.svg" alt="duck" width={100} height={100} />
          <Image src="/index/frog.svg" alt="frog" width={100} height={100} />
        </div>
      </div>
    </div>
  );
}
