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
      editable: true,
    },
    {
        field: 'test',
        headerName: 'Number in test group',
        width: 150,
        editable: true,
      },
      {
        field: 'control',
        headerName: 'Number in control group',
        width: 150,
        editable: true,
      },
      {
        field: 'description',
        headerName: 'Description',
        width: 150,
        editable: true,
      },
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
          label="Multiline"
          multiline
          rows={4}
          variant="outlined"
          style={{ width: "100%" }}
        //   defaultValue="Default Value"
          inputProps={{ style: { fontFamily: 'nunito', color: 'black'}}}
        ></CssTextField>
        {/* </FormControl> */}
       </Container> 
       <br></br>
       <Container maxWidth="sm">
    
      </Container>
    </React.Fragment>
  );
}
