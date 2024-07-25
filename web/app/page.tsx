"use client";

import { NextPage } from "next";
import { FC, useEffect, useState } from "react";
import styles from "./page.module.css";
import axios from "axios";

import { API_BASE_URL } from "web/globals";

const Home: FC = () => {
  const [message, setMessage] = useState("");

  useEffect(() => {
    axios.get(`${API_BASE_URL}/db/hello`).then((res) => {
      setMessage(res.data);
    });
  }, []);

  return (
    <main className={styles.main}>
      <p>{message}</p>
    </main>
  );
};

export default Home;
