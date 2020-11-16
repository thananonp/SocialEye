import React from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
} from '@material-ui/core';

const AppHeader = () => (
  <AppBar position="static">
    <Toolbar>
      <Typography variant="h6" color="inherit" >
        The Social Eye
      </Typography>
    </Toolbar>
  </AppBar>
);

export default AppHeader;