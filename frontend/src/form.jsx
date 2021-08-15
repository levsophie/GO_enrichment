import React from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Container from "@material-ui/core/Container";
import { DataGrid } from "@material-ui/data-grid";
import { useState, useEffect, useRef, Fetch } from "react";

const useStyles = makeStyles((theme) => ({
    root: {
      "& label.Mui-focused": {
        color: "grey",
      },
      "& .MuiInput-underline:after": {
        borderBottomColor: "black",
      },
      "& .MuiOutlinedInput-root": {
        "& fieldset": {
          borderColor: "grey",
        },
        "&:hover fieldset": {
          borderColor: "grey",
        },
        "&.Mui-focused fieldset": {
          borderColor: "black",
        },
      },
    },
  paper: {
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
  margin: {
    margin: theme.spacing(1),
  },
}));

const SignInSide = () => {
  const classes = useStyles();
  

  const [rows, setRows] = useState([]);
  const [testInput, setTestInput] = useState(null);
  const [controlInput, setControlInput] = useState(null);
  const [pageSize, setPageSize] = useState(9);
  const [page, setPage] = useState(0);
  const [significance, setSignificance] = useState(0.001)
  
  const columns = [
    { field: "id", headerName: "ID", width: 90, hide: "true" },
    {
      field: "pvalue",
      headerName: "P-value",
      width: 150,
    },
    {
      field: "test",
      headerName: "In test group",
      width: 200,
    },
    {
      field: "control",
      headerName: "In control group",
      width: 200,
    },
    {
      field: "term",
      headerName: "Term",
      width: 120,
    },
    {
      field: "description",
      headerName: "Description",
      width: 490,
    },
  ];
 
  const handleSubmit = async () => {
    console.log(testInput, significance)
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(testInput),
    };
    const response = await fetch(`/geneontology/${significance}`, requestOptions);
    if (response.status === 200) {
      const rows = await response.json();
      console.log(rows);
      setRows(rows);
    } else {
      setRows([]);
      console.log(response);
    }
  };
  let textInput = useRef(null);
  
  const handlePageSizeChange = (params) => {
    setPageSize(params.pageSize);
  };
  
 
  return (
    <React.Fragment>
    <CssBaseline />
    <AppBar color="default" variant="contained">
      <Toolbar>
        <Typography variant="h5">
          Gene set enrichment analysis for Cryptococcus neoformans var.
          grubii
        </Typography>
      </Toolbar>
    </AppBar>
    <Container maxWidth="lg">
      <Toolbar id="back-to-top-anchor" />
      <br></br>
      
      
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <Grid item xs={12} sm={8} md={6} component={Paper} >
      <div className={classes.paper}>
      <TextField
          id="test"
          label="List of identifiers for the test sample (CNAG_XXXXX)"
          multiline
          rows={4}
          inputRef={textInput}
          variant="outlined"
          style={{ width: "100%" }}
          focusedBorderColor='black'
          onChange={(e) => setTestInput(e.target.value)}
          inputProps={{ style: { fontFamily: "nunito", borderColor: "black" } }}
        ></TextField>
        <br></br><br></br>
        <TextField
          id="significance"
          label="P-value cutoff"
          multiline
          rows={1}
          inputRef={textInput}
          defaultValue={0.001}
          variant="outlined"
          style={{ width: "100%" }}
          onChange={(e) => setSignificance(e.target.value)}
          inputProps={{ style: { fontFamily: "nunito", color: "black" } }}
        ></TextField>
        
        </div>
      </Grid> 
      <Grid item xs={12} sm={8} md={6} component={Paper} >
      <div className={classes.paper}>
      <TextField
          id="control"
          label="List of identifiers for the control sample (CNAG_XXXXX)"
          multiline
          rows={4}
          inputRef={textInput}
          variant="outlined"
          style={{ width: "100%" }}
          onChange={(e) => setControlInput(e.target.value)}
          inputProps={{ style: { fontFamily: "nunito", color: "black" } }}
        ></TextField>
  
      <br></br><br></br>
      <Button
          className={classes.margin}
          type="submit"
          variant="contained"
          style={{ display: "inline block" }}
          onClick={(e) => handleSubmit(e.target.value)}
        >
          Submit
        </Button>
        {/* <Button
          className={classes.margin}
          type="submit"
          variant="contained"
          style={{ display: "inline block" }}
          onClick={() => textInput.current.value = ""}
        >
          Clear
        </Button> */}
        </div>
      </Grid> 
     
      <Grid item lg={12} sm={8} md={5} component={Paper} >
        <div className={classes.paper}>
      <Container maxWidth="lg">
        <div style={{ height: 590, width: "100%" }}>
          <DataGrid
            rows={rows}
            columns={columns}
            pageSize={5}
            disableSelectionOnClick
            autoHeight
            page={page}
            onPageChange={(params) => {
              setPage(params.page);
            }}
            pagination
            pageSize={pageSize}
            onPageSizeChange={handlePageSizeChange}
            rowsPerPageOptions={[7, 9, 20]}
            rowCount={rows.length}
          />
        </div>
      </Container>
      </div>
      </Grid>
      
    </Grid>
    
    
   
      </Container>
    </React.Fragment>
    
  );
}

export default SignInSide