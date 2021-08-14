import React from "react";
import PropTypes from "prop-types";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
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
export default function BackToTop(props) {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
        <AppBar color='transparent'>
          <Toolbar>
            <Typography variant="h6">
              Functional enrichment analysis for Cryptotccus neoformans var.
              grubii
            </Typography>
          </Toolbar>
        </AppBar>
        <Toolbar id="back-to-top-anchor" />
        <br></br>
        <FormControl className={classes.margin}></FormControl>
        <TextField
          id="standard-multiline-static"
          label="Multiline"
          multiline
          rows={4}
          variant="outlined"
          style={{ width: "100%" }}
          defaultValue="Default Value"
        ></TextField>
       </Container> 
       <br></br>
       <Container maxWidth="lg">
        <div id="comments" className={classes.customFormControl}>
          <FormControl className={classes.textField}>
            <TextField
              id="outlined-textarea"
              label="Multiline Placeholder"
              placeholder="Placeholder"
              multiline
              rows={4}
              style={{ width: "100%" }}
              variant="outlined"
              inputProps={{ className: classes.textarea }}
            />
          </FormControl>
        </div>
      </Container>
    </React.Fragment>
  );
}
