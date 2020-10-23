import * as firebase from "firebase/app";
import "firebase/database";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDlsOJK_IyiZEhP3vAIfR0VQK3N4she84U",
    authDomain: "socialeye-seniorproject.firebaseapp.com",
    databaseURL: "https://socialeye-seniorproject.firebaseio.com",
    projectId: "socialeye-seniorproject",
    storageBucket: "socialeye-seniorproject.appspot.com",
    messagingSenderId: "209273349716",
    appId: "1:209273349716:web:06abba1d7cb9e2a67f6fc1",
    measurementId: "G-T04J1XK538"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const database = firebase.database();
  
  export { database }