<template>
  <header class="app-header">
    <router-link to="/dashboard">
      <img src="@/assets/logo2.png" alt="Logo" class="logo-2" />
    </router-link>
    <nav>
      <router-link class="btn" :to="buttonLink">{{ buttonText }}</router-link>
    </nav>
  </header>
</template>

<script>
export default {
  name: "Header",
  computed: {
    buttonLink() {
      return this.$route.path === "/create-area" ? "/dashboard" : "/create-area";
    },
    buttonText() {
      return this.$route.path === "/create-area" ? "Back to dashboard" : "Create an area";
    },
  },
};
</script>

<style>
.logo-2 {
  width: 70px;
}

.app-header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  font-family: 'LeagueSpartan', serif;
  height: 80px;
  background-color: var(--main-primary-color);
  color: white;
}

.btn {
  background-color: var(--color-complementary-1);
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-size: 16px;
  margin-left: 20px;
  transition: transform 0.2s ease-in-out;
}

.btn:hover {
  background-color: var(--color-complementary-2);
  transform: scale(1.1);
}

</style>