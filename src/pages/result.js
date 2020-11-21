import React, { useEffect, useState } from "react";
import _ from "lodash";

import "../App.css";
import { database } from "../config/firebase";

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
  Text,
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
    minWidth: 300,
  },
});

export const LandResultTable = () => {
  const [data, setData] = useState();
  const [alreadyQuery, setAlreadyQuery] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const result = await database
        .ref("/result")
        .once("value")
        .then(function (snapshot) {
          return snapshot.val();
        });
      setData(result);
      setAlreadyQuery(true);
    };
    if (!alreadyQuery) {
      fetchData();
    }
    if (data) {
      console.log("Mockup ", data);
    }
  });
  // console.log(mockxxx)

  console.log("Data ", data);

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

  const renderData = () => {
    if (data)
      return (
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
                  <TableCell style={{ width: 800 }}>Name</TableCell>
                  <TableCell>Price</TableCell>
                  <TableCell>Link</TableCell>
                  <TableCell>Link</TableCell>
                  <TableCell>Link</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data
                  .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                  .map((data, key) => {
                    return (
                      <Stock
                        key={key}
                        name={data.title}
                        catagory={data.category}
                        price={data.price}
                        size={data.size}
                        link={data.link}
                        source={data.source}
                        pubDate={data.pubDate}
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
      );
    return <h1>กูโหลดอยู่ไอ่สัส!!!</h1>;
  };
  // const stringJSON = JSON.stringify(database)
  // console.log("database ", database)
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
      {renderData()}
    </>
  );
};

const HomePageHeader = () => {
  return (
    <header className="header">
      <Typography variant="h4" className="header" style={{ padding: 10 }}>
        Result for "Saimai"
      </Typography>
    </header>
  );
};

const Stock = ({ name, catagory, price, size, link, source, pubDate }) => {
  // if (!name) return null;
  return (
    <TableRow>
      <TableCell>{name}</TableCell>
      <TableCell>{catagory}</TableCell>
      <TableCell>{price}</TableCell>
      <TableCell>{source}</TableCell>
      <TableCell>{pubDate}</TableCell>
      <TableCell>
        <a href={link}>Link</a>
      </TableCell>
    </TableRow>
  );
};
