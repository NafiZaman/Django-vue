<template>
  <div>
    <NavBar />
    <router-view />
    <Footer />
    <GotoTop />
  </div>
</template>

<script>
import axios from "axios";
import NavBar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
import GotoTop from "./components/GotoTop.vue";

export default {
  name: "App",
  components: {
    NavBar,
    Footer,
    GotoTop,
  },
  beforeCreate() {
    this.$store.commit("INIT_STORE");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>