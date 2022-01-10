<template>
  <div class="home">
    <NowShowing />
    <Promos />
    <Social />
    <!-- <Footer /> -->
  </div>
</template>

<script>
import NowShowing from "@/components/NowShowing.vue";
import Promos from "@/components/Promos.vue";
import Social from "@/components/Social.vue";
// import Footer from "@/components/Footer.vue";

export default {
  name: "Home",
  components: {
    NowShowing,
    Promos,
    Social,
    // Footer,
  },
};
</script>
