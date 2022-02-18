<template>
  <div>
    <div
      id="back-to-top"
      class="
        hidden
        bg-black
        text-white
        shadow-lg shadow-gray-900/50
        fixed
        z-30
        bottom-0
        right-0
        mr-6
        mb-6
        rounded-full
      "
      @click="gotoTop"
      @scroll="checkScrollPosition"
    >
      <a href="#" class="">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-10 w-10"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 15l7-7 7 7"
          />
        </svg>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "GotoTop",
  data() {
    return {};
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    gotoTop(event) {
      event.preventDefault();
      window.scroll({ top: 0, left: 0, behavior: "smooth" });
    },
    onScroll(event) {
      event.preventDefault();
      const backToTop = document.querySelector("#back-to-top");
      if (event.target.documentElement.scrollTop >= 500) {
        // console.log("asdasdasd");
        backToTop.classList.remove("hidden");
        backToTop.classList.add("block");
      } else {
        backToTop.classList.add("hidden");
        backToTop.classList.remove("block");
      }
    },
  },
};
</script>