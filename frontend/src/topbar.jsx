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
import { DataGrid } from '@material-ui/data-grid';
import { Button } from "@material-ui/core";

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
    width: "100ch"
  },
}));

const CssTextField = withStyles({
    root: {
      '& label.Mui-focused': {
        color: 'grey',
      },
      '& .MuiInput-underline:after': {
        borderBottomColor: 'black',
      },
      '& .MuiOutlinedInput-root': {
        '& fieldset': {
          borderColor: 'grey',
        },
        '&:hover fieldset': {
          borderColor: 'grey',
        },
        '&.Mui-focused fieldset': {
          borderColor: 'black',
        },
      },
    },
  })(TextField);

export default function TopBar(props) {
  const classes = useStyles();

  const columns = [
    { field: 'id', headerName: 'ID', width: 90, hide: 'true' },
    {
      field: 'pvalue',
      headerName: 'P-value',
      width: 150,
    },
    {
        field: 'test',
        headerName: 'In test group',
        width: 200,
      },
      {
        field: 'control',
        headerName: 'In control group',
        width: 200,
      },
      {
        field: 'description',
        headerName: 'Description',
        width: 500,
      },
]

const rows = [
    { id: 1, pvalue: 0.0004, test: 10, control: 10, description: "very interesting GO group" },
]

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar color='transparent' variant="contained">
          <Toolbar>
            <Typography variant="h5">
              Functional enrichment analysis for Cryptotccus neoformans var.
              grubii
            </Typography>
          </Toolbar>
          </AppBar>
      <Container maxWidth="sm">
        <Toolbar id="back-to-top-anchor" />
        <br></br><br></br>
        {/* <FormControl className={classes.margin}> */}
        <CssTextField
          id="standard-multiline-static"
          label="List of identifiers (CNAG_XXXXX)"
          multiline
          rows={4}
          variant="outlined"
          style={{ width: "100%" }}
        //   defaultValue="Default Value"
          inputProps={{ style: { fontFamily: 'nunito', color: 'black'}}}
        ></CssTextField>
        {/* </FormControl> */}
        <Button
            className={classes.margin}
            type="submit"
            variant = "contained"
            style={{ display: "inline block" }}
          >
            Submit
          </Button>
          <Button
            className={classes.margin}
            type="submit"
            variant = "contained"
            style={{ display: "inline block" }}
          >
            Clear
          </Button>
       </Container> 
       <br></br>
       <Container maxWidth="lg">
       <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        disableSelectionOnClick
        autoHeight
      />
    </div>
      </Container>
    </React.Fragment>
  );
}
