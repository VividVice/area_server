// create a global variable to store the base url and then export it so it can be used in other files`

let Url = "http://192.168.1.63:8080";

const ServerUrl = () => Url;

const setServerUrl = (newUrl) => {
  Url = newUrl;
};

export { ServerUrl, setServerUrl };
