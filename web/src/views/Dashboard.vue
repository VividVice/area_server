<template>
  <div class="dashboard">
    <img src="@/assets/logo.png" alt="Logo de mon application" class="logo">
    <h2 class="appName">Dashboard</h2>
    <p class="slogan">Connect your apps together</p>
    <router-link class="btn" to="/create-area" >Add new area</router-link>

    <h2 class="title">Your areas</h2>
    <div class="area">
      <div class="area-icon">
        <img src="@/assets/appIcons/spotify-icon.png" alt="Spotify Logo" class="app-icon" style="margin-right: 10px;">
        <img src="@/assets/appIcons/trello-icon.png" alt="Trello Logo" class="app-icon">
      </div>
      <div class="area-text">
        <p>Add attachment to card in Trello when new card</p>
      </div>
      <div class="switch">
        <input type="checkbox" id="toggleSwitch">
        <label for="toggleSwitch" class="slider"></label>
      </div>
    </div>

    <h2 class="title">Recommended areas</h2>
    <div class="area">
      <div class="area-icon">
        <img src="@/assets/appIcons/spotify-icon.png" alt="Spotify Logo" class="app-icon" style="margin-right: 10px;">
        <img src="@/assets/appIcons/trello-icon.png" alt="Trello Logo" class="app-icon">
      </div>
      <div class="area-text">
        <p>Add attachment to card in Trello when new card</p>
      </div>
      <div class="area-btn">
        <button>Try it</button>
      </div>
    </div>

    <div class="area">
      <div class="area-icon">
        <img src="@/assets/appIcons/spotify-icon.png" alt="Spotify Logo" class="app-icon" style="margin-right: 10px;">
        <img src="@/assets/appIcons/trello-icon.png" alt="Trello Logo" class="app-icon">
      </div>
      <div class="area-text">
        <p>Add attachment to card in Trello when new card</p>
      </div>
      <div class="area-btn">
        <button>Try it</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    token() {
      return localStorage.getItem('user-token')
    }
  }
}
</script>

<style>

.dashboard {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-bottom: 50px;
}

.btn {
  padding: 10px 20px;
  background-color: var(--color-complementary-1);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  text-decoration: none;
  font-family: 'Quicksand_Light', serif;
  transition: background-color 0.3s ease, transform 0.4s ease;
}

.btn:hover {
  transform: scale(1.2);
}


.logo {
  width: 150px;
}

.appName {
  margin-top: 0px;
  margin-bottom: 10px;
  font-family: 'LeagueSpartan', serif;
  font-size: 45px;
}

.slogan {
  margin-bottom: 40px;
  font-family: 'Quicksand_Light', serif;
  font-size: 20px;
}

.title {
  margin-bottom: 20px;
  font-family: 'LeagueSpartan', serif;
  font-size: 30px;
  align-self: start;
  margin-left: 25%;
}

.area {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 80%;
  font-family: 'Quicksand_Light', serif;
  max-width: 800px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 5px;
  background-color: #EFA7A8;
}

.area-icon {
  width: 20%;
}

.area-icon img {
  width: 20%;
}

.area-text {
  width: 60%;
}

.area-btn {
  width: 20%;
}

.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: var(--main-primary-color)
}

input:checked + .slider:before {
  transform: translateX(26px);
}

</style>