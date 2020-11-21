import React, { Fragment } from "react";
import logo from "../architectsolid.svg";
import {
  Button,
  TextField,
  makeStyles,
  Typography,
  Container,
} from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams,
} from "react-router-dom";
import EnhancedTable from "./result1";
import "../App.css";
import AppHeader from "../components/AppHeader"

export const Search = () => {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} alt="logo" />
        <Typography variant="h3" className="header">The social eye</Typography>
        <form noValidate autoComplete="off">
          <TextField id="standard-basic" label="Search" />
        </form>
        <br />
        <Link to="/result">
          <Button variant="contained" color="primary">Go</Button>
        </Link>
      </header> */}
      <AppHeader>
        <EnhancedTable />
      </AppHeader>
    </div>
  );
};
