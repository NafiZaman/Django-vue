<template>
  <nav
    class="d-sm-block d-md-none p-0 navbar bg-danger text-light fixed-bottom"
  >
    <div
      class="row align-items-center justify-content-center"
      v-for="(item, index) in buttonIcons"
      :key="index"
    >
      <a
        class="mt-2 mb-0 text-center text-decoration-none text-light h2"
        href="#"
        ><i :class="item.icon"></i
      ></a>
      <p class="text-center p-0 m-0">
        <small>{{ item.text }}</small>
      </p>
    </div>
  </nav>
</template>

<script>
export default {
  name: "BottomMenu",
  data() {
    return {
      buttonIcons: [
        {
          text: "Spotlight",
          icon: "bi bi-lightning-charge-fill",
        },
        {
          text: "Movies",
          icon: "bi bi-camera-reels-fill",
        },
        {
          text: "Theatres",
          icon: "bi bi-ticket-perforated-fill",
        },
        {
          text: "Account",
          icon: "bi bi-person-fill",
        },
      ],
    };
  },
};
</script>
