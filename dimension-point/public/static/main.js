// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDxxaT1zv7OjPdMxCSBaNXmL1KNUYlpxBE",
  authDomain: "dimension-point.firebaseapp.com",
  projectId: "dimension-point",
  storageBucket: "dimension-point.appspot.com",
  messagingSenderId: "954591020307",
  appId: "1:954591020307:web:7fceb7d37ea2a2d15c46e6",
  measurementId: "G-KH1T0CTM9F"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);