<template>
  <div>
    <img src="@/assets/logo.png" alt="Logo de mon application" class="logo">
    <h2 class="appName">AreaCraft.</h2>
    <h2 class="slogan">Log in to your account</h2>

    <!-- <GoogleLogin @onclick="login" />

    <h2 class="slogan">or</h2> -->
    <div class="input-container">
      <i class="fas fa-user icon"></i>
      <input v-model="username" placeholder="Username">
    </div>
    <div class="input-container">
      <i class="fas fa-lock icon"></i>
      <input type="password" v-model="password" placeholder="Password">
    </div>
    <div class="message">{{ message }}</div>
    <div class="rememberMe">
      <input type="checkbox" v-model="rememberMe"> Remember me
      <button class="create-account-button" @click="register">Create account</button>
    </div>
    <div>
      <button @click="login">Login</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
      message: '',
      rememberMe: false,
    };
  },
  methods: {
    login() {
      if (this.username === '' || this.password === '') {
        alert('Please fill in all fields');
        return;
      } else {
        fetch('http://51.20.135.59:80/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
            rememberMe: this.rememberMe,
          }),
        })
          .then((response) => {
            if (response.status === 200) {
              return response.json();
            } else if (response.status === 401) {
              alert('Incorrect username or password');
            } else {
              alert('Error:', response.status);
            }
          })
          .then((data) => {
            if (data) {
              localStorage.setItem('user-token', data.token);
              this.$router.push('/dashboard');
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
        }
    },
    register() {
      if (this.username === '' || this.password === '') {
        this.message = 'Please fill in all fields';
        return;
      } else {
        fetch('http://51.20.135.59:80/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        })
          .then((response) => {
            if (response.status === 201) {
              this.message = 'Registration successful';
            } else if (response.status === 409) {
              this.message = 'Username already exists';
            } else {
              this.message = `Error: ${response.status}`;
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
        }
    },
  }
}
</script>

<style>
.logo {
  width: 150px;
}

.appName {
  margin-top: 0px;
  margin-bottom: 10px;
  font-family: 'LeagueSpartan', serif;
  font-size: 45px;
}

.message {
  margin-bottom: 10px;
  font-family: 'Quicksand_Light', serif;
  font-size: 16px;
  color: var(--color-complementary-1);
}

.slogan {
  margin-bottom: 40px;
  font-family: 'Quicksand_Light', serif;
  font-size: 20px;
}

.input-container {
  position: relative;
  margin-bottom: 15px;
}

.input-container input {
  padding-left: 40px;
  padding: 10px;
  width: 20%;
  border-radius: 5px;
  font-size: 16px;
  font-family: 'LeagueSpartan', serif;
  background-color: white;
}

.input-container .icon {
  position: absolute;
  left: 37%;
  top: 50%;
  transform: translateY(-50%);
  color: var(--main-primary-color);
}

.create-account-button {
  padding: 5px 10px;
  margin-bottom: 15px;
  margin-left: 13%;
  background-color: var(--primary);
  color: var(--main-primary-color);
  border: none;
  border-radius: 5px;
  font-family: 'LeagueSpartan', serif;
  cursor: pointer;
  font-size: 14px;
}

.rememberMe {
  margin-bottom: 15px;
  font-family: 'Quicksand_Light', serif;
  margin-left: 30%;
  margin-right: 30%;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  background-color: var(--color-complementary-1);
  color: white;
  border: none;
  border-radius: 5px;
  font-family: 'LeagueSpartan', serif;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  animation: pulse 0.5s infinite alternate;
}

@keyframes pulse {
  from {
    transform: scale(1);
  }

  to {
    transform: scale(1.1);
  }
}

.google-div {
  margin-bottom: 15px;
  width: 25%;
  align-self: center;
}


</style>