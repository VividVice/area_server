<template>
  <div id="app">
    <Header v-if="!isLoginPage" />
    <router-view />
    <Footer v-if="!isLoginPage" />
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  components: {
    Header,
    Footer
  },
  computed: {
    isLoginPage() {
      return this.$route.name === 'login';
    }
  }
}
</script>

<style>
body {
  background-color: var(--main-bg-color);
  color: var(--main-text-color);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
@font-face {
  font-family: 'Quicksand_Light';
  src: url('./assets/fonts/Quicksand_Light.otf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'LeagueSpartan';
  src: url('./assets/fonts/LeagueSpartan-Bold.otf') format('truetype');
  font-weight: bold;
  font-style: normal;
}
</style>
