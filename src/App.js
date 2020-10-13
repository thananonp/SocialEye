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