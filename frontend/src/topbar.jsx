import React from "react";
import PropTypes from "prop-types";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { makeStyles, withStyles } from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import useScrollTrigger from "@material-ui/core/useScrollTrigger";
import Box from "@material-ui/core/Box";
import Container from "@material-ui/core/Container";
import Fab from "@material-ui/core/Fab";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";
import Zoom from "@material-ui/core/Zoom";
import { FormControl, TextField } from "@material-ui/core";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import InputAdornment from "@material-ui/core/InputAdornment";
import Grid from "@material-ui/core/Grid";
import AccountCircle from "@material-ui/icons/AccountCircle";
import { TextareaAutosize, Select, MenuItem } from "@material-ui/core/";
import DateFnsUtils from "@date-io/date-fns";
import { useHistory } from "react-router-dom";
import { DataGrid } from "@material-ui/data-grid";
import { Button } from "@material-ui/core";
import { useState, useEffect, useRef, Fetch } from "react";
import ScrollDialog from "./dialog";
import { Link } from 'react-router-dom';
import { Redirect } from "react-router";
import { Dialog } from "@material-ui/core";
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

const useStyles = makeStyles((theme) => ({
  root: {
    "& .MuiTextField-root": {
      margin: theme.spacing(1),
      width: "25ch",
    },
  },
  margin: {
    margin: theme.spacing(1),
  },
  textarea: {
    resize: "both",
    width: "100ch",
  },
}));

const CssTextField = withStyles({
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
})(TextField);

export default function TopBar(props) {
  const classes = useStyles();
  const [rows, setRows] = useState([]);
  const [input, setInput] = useState();
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
      renderCell: (params) => (
        <div style={{ color: "blue" }}>
        {params.value}
            </div>
       )},
    {
      field: "description",
      headerName: "Description",
      width: 500,
    },
  ];
  // useEffect(() => {
  //   setRows();
  // }, []);

  const handleSubmit = async () => {
    console.log(input, significance)
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(input),
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
  const history = useHistory();
    
  const [open, setOpen] = useState(false);
  const [scroll, setScroll] = useState('paper');
  const [currentTerm, setCurrentTerm] = useState()
  const [currentTermDescription, setCurrentTermDescription] = useState()
  const [listOfGenes, setListOfGenes] = useState([])

  const handleClose = () => {
    setOpen(false);
  };
  
  const descriptionElementRef = React.useRef(null);
  React.useEffect(() => {
    if (open) {
      const { current: descriptionElement } = descriptionElementRef;
      if (descriptionElement !== null) {
        descriptionElement.focus();
      }
    }
  }, [open]);
  
    const handleCellClick = async (param, event) => {
      console.log(param);
      console.log(event);
      if (param.colDef.field === 'term'){
        console.log("GO term", param.row.term) 
        let term = param.row.term
        window.open(`https://www.ebi.ac.uk/QuickGO/term/${term}`) 
      } 
      else {
        setOpen(true);
        setCurrentTerm(param.row.term) 
        setCurrentTermDescription(param.row.description) 
      let data = {
        gene_list: input,
        term: param.row.term,
      };
      console.log(input, param.row.term);
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      };
      const response = await fetch("/geneontology/terms", requestOptions);
      if (response.status === 200) {
        const resp = await response.json();
        console.log(resp);
        
      
      if (param.colDef.field === 'test') {
        console.log('display test group', resp.test);
        setListOfGenes(resp.test)
        // setScroll(scrollType);
        // ScrollDialog(param.row.test)
      } else {
        console.log('display control group', resp.control);
        setListOfGenes(resp.control)
      }
      }  
    }
       event.stopPropagation();
    };
  
  
  
  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar color="default" variant="contained">
        <Toolbar>
          <Typography variant="h5">
            Gene set functional enrichment analysis for Cryptococcus neoformans var.
            grubii
          </Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="sm">
        <Toolbar id="back-to-top-anchor" />
        <br></br>
        
        <CssTextField
          id="standard-multiline-static"
          label="List of identifiers (CNAG_XXXXX)"
          multiline
          rows={4}
          inputRef={textInput}
          variant="outlined"
          style={{ width: "100%" }}
          onChange={(e) => setInput(e.target.value)}
          inputProps={{ style: { fontFamily: "nunito", color: "black" } }}
        ></CssTextField>
        <br></br><br></br>
        <CssTextField
          id="standard-multiline-static"
          label="P-value cutoff"
          multiline
          rows={1}
          // inputRef={textInput}
          defaultValue={0.001}
          variant="outlined"
          style={{ width: "100%" }}
          onChange={(e) => setSignificance(e.target.value)}
          inputProps={{ style: { fontFamily: "nunito", color: "black" } }}
        ></CssTextField>
         
         <Button
          className={classes.margin}
          type="submit"
          variant="contained"
          style={{ display: "inline block" }}
          onClick={(e) => handleSubmit(e.target.value)}
        >
          Submit
        </Button>
        <Button
          className={classes.margin}
          type="submit"
          variant="contained"
          style={{ display: "inline block" }}
          onClick={() => textInput.current.value = ""}
        >
          Clear
        </Button>
      </Container>
      <br></br>
      <Container maxWidth="lg">
        <div style={{ height: 400, width: "100%" }}>
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
            onCellClick={handleCellClick}
          />
        </div>
 
        <div>
          <Dialog
          open={open}
          onClose={handleClose}
          scroll={scroll}
          aria-labelledby="scroll-dialog-title"
          aria-describedby="scroll-dialog-description"
        >
          <DialogTitle id="scroll-dialog-title">{currentTerm} - {currentTermDescription}</DialogTitle>
          <DialogContent dividers={scroll === 'paper'}>
            <DialogContentText
              id="cnag"
              ref={descriptionElementRef}
              tabIndex={-1}
            >{
              listOfGenes.map(dataIn => (
                <div key={dataIn.cnag}>
                  <Typography variant="body2" component={'span'} color="textPrimary">
                    {`${dataIn.cnag} ${dataIn.function}`}
                  </Typography>
                  </div>
               ))  
            }
              
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleClose} color="primary">
              Close
            </Button>
          </DialogActions>
        </Dialog>
      </div>
      </Container>
    </React.Fragment>
    
  );
}
