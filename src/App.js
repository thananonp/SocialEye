import React, { Fragment } from 'react';
import {
  CssBaseline,
  withStyles,
} from '@material-ui/core';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import AppHeader from './components/AppHeader';
import { LandResultTable } from "./pages/result";
import "./App.css";
import "./pages/search.js"
import { Search } from "./pages/search.js";

// Firebase App (the core Firebase SDK) is always required and must be listed first
import * as firebase from "firebase/app";

// If you enabled Analytics in your project, add the Firebase SDK for Analytics
import "firebase/analytics";

// Add the Firebase products that you want to use
import "firebase/auth";
import "firebase/firestore";

const styles = theme => ({
  main: {
    padding: theme.spacing(3),
    [theme.breakpoints.down('xs')]: {
      padding: theme.spacing(2),
    },
  },
});

const App = ({ classes }) => (
  <Fragment>
    <CssBaseline />
    <AppHeader />
    <main className={classes.main}>
      <Router>
        <div>

          <Switch>
            <Route path="/result">
              <Result />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    </main>
  </Fragment>
);

export default withStyles(styles)(App);

// // export default function App() {
//   return (
//     <Router>
//       <div>

//         <Switch>
//           <Route path="/result">
//             <Result />
//           </Route>
//           <Route path="/">
//             <Home />
//           </Route>
//         </Switch>
//       </div>
//     </Router>
//   );
// }

function Home() {
  return <div className="App">
    < Search />
  </div>
}

function Result() {
  return (
    <div className="App">
      < LandResultTable />
    </div>
  );
}

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