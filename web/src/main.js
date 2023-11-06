import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/variables.css';
import './assets/fonts/styles.css';
import vue3GoogleLogin from 'vue3-google-login'

const app = createApp(App);

app.use(router);
app.use(vue3GoogleLogin, {
    clientId: '621956430343-i2662af5mf8ni6fnu18itodqn5oetoto.apps.googleusercontent.com'
})
app.mount('#app');