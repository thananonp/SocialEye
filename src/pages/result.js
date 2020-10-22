import React from "react";
import "../App.css";
// import { stockData } from "../mockupjson";
import data from '../teedin108.json'

import {
  Button,
  TextField,
  makeStyles,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TablePagination,
  Paper,
} from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams,
} from "react-router-dom";
import "fontsource-roboto";

const useStyles = makeStyles({
  table: {
    Width: 300,
  },
});


export const LandResultTable = () => {
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  return (
    <>
      <HomePageHeader />
      <Link to="/">
        <Button
          variant="outlined"
          color="primary"
          href="#outlined-buttons"
          style={{ margin: 10 }}
        >
          Home
        </Button>
      </Link>
      <Link to={"/mockupjson.js"} target="_blank" download>
        <Button variant="contained" color="primary">
          Download JSON
        </Button>
      </Link>
      <Paper elevation={3}>
        <TableContainer>
          <Table
            stickyHeader
            className={classes.table}
            aria-label="simple table"
            size="small"
          >
            <TableHead>
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell align="center">Price</TableCell>
                <TableCell align="center">Link</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {data
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((data, key) => {
                  return (
                    <Stock
                      key={key}
                      name={data.name}
                      price={data.price}
                      // size={data.size}
                      // persquaremeter={data.persquaremeter}
                      // location={data.location}
                      // district={data.district}
                      // province={data.province}
                      // comparison={data.comparisonwithaverage}
                      link={data.link}
                    />
                  );
                })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[10, 25, 100]}
          component="div"
          count={data.length}
          rowsPerPage={rowsPerPage}
          page={page}
          onChangePage={handleChangePage}
          onChangeRowsPerPage={handleChangeRowsPerPage}
        />
      </Paper>
    </>
  );
};

const HomePageHeader = () => {
  return (
    <header className="header">
      {/* <Typography variant="h2" className="header">
        The Social Eye
      </Typography> */}
      <Typography variant="h4" className="header" style={{padding: 10}}>
        Result for "Saimai"
      </Typography>
    </header>
  );
};

const Stock = ({
  name,
  price,
  size,
  persquaremeter,
  location,
  district,
  province,
  comparison,
  link,
}) => {
    // if (!name) return null;
  return (
    <TableRow>
      <TableCell>{name}</TableCell>
      <TableCell>{price}</TableCell>
      {/* <TableCell>{size}</TableCell>
      <TableCell>{persquaremeter}</TableCell>
      <TableCell>{location}</TableCell>
      <TableCell>{district}</TableCell>
      <TableCell>{province}</TableCell>
      <TableCell>{comparison}</TableCell> */}
      <TableCell>
        <a href={link}>Link</a>
      </TableCell>
    </TableRow>
  );
};
