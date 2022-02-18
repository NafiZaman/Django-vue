<template>
  <div class="home">
    <BannerAd />
    <Featured />
    <Display />
  </div>
</template>

<script>
import BannerAd from "../components/BannerAd.vue";
import Featured from "../components/Featured.vue";
import Display from "../components/Display.vue";

export default {
  name: "Home",
  components: {
    BannerAd,
    Featured,
    Display,
  },
};
</script>