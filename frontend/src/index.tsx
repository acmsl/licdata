import "./styles/tailwind.scss";
import { render } from "solid-js/web";
import { Router, Route } from "@solid-app/router";

import App from "./App";

render(() => (
    <Router>
        <Route path="/" component={App} />
    </Router>
), document.getElementById("app"));
