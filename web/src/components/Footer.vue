<template>
  <footer class="app-footer">
    <p>&copy; 2023 AreaCraft. Tous les droits sont réservés.</p>
    <a href="#" class="back-to-login" @click="backToLogin">Back to Login</a>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    backToLogin() {
      this.$router.push('/');
    },
  },
};
</script>

<style>
.app-footer {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  height: 80px;
  background-color: var(--main-primary-color);
  color: white;
}

.back-to-login {
  color: white;
  text-decoration: underline;
  cursor: pointer;
}

.back-to-login:hover {
  color: #4a9199;
}
</style>