<template>
  <div id="nav">
    <InfoBar />
    <NavBar />
    <router-view />
    <Footer />
    <BottomMenu />
  </div>
</template>

<script>
import axios from "axios";
import "../node_modules/bootstrap/dist/js/bootstrap.min.js";
import InfoBar from "@/components/InfoBar.vue";
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import BottomMenu from "@/components/BottomMenu.vue";

export default {
  name: "App",
  components: {
    InfoBar,
    NavBar,
    Footer,
    BottomMenu,
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
    const token = this.$store.state.token;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
  // methods: {
  //   // logout() {
  //   //   axios
  //   //     .post("/api/account/logout/")
  //   //     .then((response) => {
  //   //       axios.defaults.headers.common["Authorization"] = "";
  //   //       localStorage.removeItem("token");
  //   //       this.$store.commit("removeToken");
  //   //       this.$router.push("/");
  //   //     })
  //   //     .catch((error) => {
  //   //       if (error.response) console.log(JSON.stringify(error.response.data));
  //   //       else if (error.message) console.log(JSON.stringify(error.message));
  //   //       else console.log(JSON.stringify(error));
  //   //     });
  //   // },
  // },
};
</script>

<style lang="scss">
@import "../node_modules/bootstrap";
@import "../node_modules/bootstrap-icons/font/bootstrap-icons.css";
</style>
