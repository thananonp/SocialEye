import React from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  IconButton,
} from '@material-ui/core';
import { fade, makeStyles } from '@material-ui/core/styles';
// import MenuIcon from '@material-ui/icons/Menu';
// import SearchIcon from '@material-ui/icons/Search';
import logo from './images/Icon.png';

const AppHeader = () => (
  <AppBar position="static">
    <Toolbar>
      <img
        src={logo}
        alt="logo"
        width="50"
        height="50"
        style={{ marginRight: 10 }}
      />
      <Typography variant="h6" color="inherit">
        Social Eye
      </Typography>
    </Toolbar>
  </AppBar>
);

export default AppHeader;