<template>
  <footer class="app-footer">
    <p>&copy; 2023 AreaCraft. Tous les droits sont réservés.</p>
    <button @click="downloadMobileVersion">Download Mobile Version</button>
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
      downloadMobileVersion() {
        fetch('http://51.20.135.59:80/client.apk', { // Changed to match the server's endpoint
          method: 'GET'
        })
        .then(response => response.blob())
        .then(blob => {
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.style.display = 'none';
          a.href = url;
          a.download = 'client.apk'; // You might want to change this to 'w.apk' to reflect the server's file name
          document.body.appendChild(a);
          a.click();
          window.URL.revokeObjectURL(url);
          document.body.removeChild(a); // It's a good practice to clean up and remove the element after the download has started
        })
        .catch((error) => {
          console.error('Error:', error);
        });
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