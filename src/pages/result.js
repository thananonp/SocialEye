import React from "react";
import "../App.css";
import { stockData } from "../mockupjson";
import { Button, TextField, makeStyles, Typography } from '@material-ui/core';
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
    useRouteMatch,
    useParams
} from "react-router-dom";
import 'fontsource-roboto';

export const LandResultTable = () => {
    return (
        <>
            <br />



            <HomePageHeader />

            <Link to="/" >
                <Button variant="outlined" color="primary" href="#outlined-buttons">
                    Home
                </Button>
            </Link>
            <Link to={"/mockupjson.js"} target="_blank" download><Button variant="contained" color="primary">
                Download JSON
            </Button>
            </Link>
            <table class="result">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Price (THB)</th>
                        <th>Size</th>
                        <th>Price per square meter (THB)</th>
                        <th>Location</th>
                        <th>District</th>
                        <th>Province</th>
                        <th>Comparison</th>
                        <th>Source</th>
                    </tr>
                </thead>
                {stockData.map((data, key) => {
                    return (
                        <Stock
                            key={key}
                            name={data.name}
                            price={data.price}
                            size={data.size}
                            persquaremeter={data.persquaremeter}
                            location={data.location}
                            district={data.district}
                            province={data.province}
                            comparison={data.comparisonwithaverage}
                            source={data.source}
                        />

                    );
                })}
            </table>
        </>
    );
};

const HomePageHeader = () => {
    return (
        <header className="header">
            <Typography variant="h2" className="header">The social eye</Typography>
            <Typography variant="h4" className="header">Result for "Saimai"</Typography>

        </header>
    );
};
const Stock = ({ name, price, size, persquaremeter, location, district, province, comparison, source }) => {
    if (!name) return <div />;
    return (
        <tbody>
            <tr>
                <td>
                    <h5>{name}</h5>
                </td>
                <td>
                    <h5>{price}</h5>
                </td>
                <td>
                    <h5>{size}</h5>
                </td>
                <td>
                    <h5>{persquaremeter}</h5>
                </td>
                <td>
                    <h4>{location}</h4>
                </td>
                <td>
                    <p>{district}</p>
                </td>
                <td>
                    <p>{province}</p>
                </td>
                <td>
                    <p>{comparison}</p>
                </td>
                <td>
                    <a href={source}> web </a>
                </td>
            </tr>
        </tbody>

    );
};