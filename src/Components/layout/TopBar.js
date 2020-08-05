import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Popover from '@material-ui/core/Popover';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import { Link } from 'react-router-dom'

export default function TopBar(props) {

    const useStyles = makeStyles((theme) => ({
        root: {
            flexGrow: 1,
        },
        menuButton: {
            marginRight: theme.spacing(2),
        },
        title: {
            flexGrow: 1,
        },
        typography: {
            padding: theme.spacing(2),
        }
    }));

    const classes = useStyles();
    const [anchorEl, setAnchorEl] = React.useState(null);
 
    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };

    const handleClose = () => {
        setAnchorEl(null);
    };

    const { name1, page1, name2, page2 } = props.links
    const open = Boolean(anchorEl);
    const id = open ? 'simple-popover' : undefined;

    return (
        <div>
            <div className={classes.root}>
                <AppBar position="static">
                    <Toolbar>
                    <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu" onClick={handleClick}>
                        <MenuIcon />
                    </IconButton>
                    <Typography variant="h6" className={classes.title}>
                        MealPlan
                    </Typography>
                    <Button color="inherit">Login</Button>
                    </Toolbar>
                </AppBar>
                <Popover
                    id={id}
                    open={open}
                    anchorEl={anchorEl}
                    onClose={handleClose}
                    anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'center',
                    }}
                    transformOrigin={{
                    vertical: 'top',
                    horizontal: 'center',
                    }}
                >
                    <MenuItem><Link style={{textDecoration: 'none', color: 'black'}} to={page1}>{name1}</Link></MenuItem>
                    <MenuItem><Link style={{textDecoration: 'none', color: 'black'}} to={page2}>{name2}</Link></MenuItem>
                    <MenuItem><Link style={{textDecoration: 'none', color: 'black'}} to='/logout'>Logout</Link></MenuItem>
                </Popover>
            </div>
        </div>
    );
}

// let image = {
//     backgroundImage: `url(${dhall})`,
//     backgroundPosition: 'center',
//     backgroundSize: 'cover',
//     height: '100vw',
//     width: '100vw'
//   }

