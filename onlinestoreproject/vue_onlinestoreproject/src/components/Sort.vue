<template>
  <div class="ml-auto">
    <button class="drop-down-button" id="menu-btn" @click="toggleMenu()">
      <div class="flex">
        <p class="font-medium mr-1">Sort by:</p>
        <p>{{ currentSortType }}</p>
      </div>
      <svg
        class="ml-2 w-4 h-4"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 9l-7 7-7-7"
        ></path>
      </svg>
    </button>
    <div
      id="sort-drop-down"
      class="bg-white mt-1 py-1 absolute shadow-2xl hidden flex-col text-sm"
    >
      <button
        class="px-3 py-2 hover:bg-black hover:text-white text-left"
        v-for="(name, sortType) in sortTypes"
        :key="sortType"
        @click="onClickSortOption(sortType)"
      >
        {{ name }}
      </button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "Sort",
  data() {
    return {
      sortTypes: {
        default: "Best Matches",
        minMax: "Price Low To High",
        maxMin: "Price High To Low",
        alphaAsc: "Product Name A - Z",
        alphaDesc: "Product Name Z - A",
        rating: "Most Popular",
      },
      currentSortType: "",
    };
  },
  mounted() {
    this.setCurrentSortType("default");
  },
  computed: {
    ...mapGetters(["filters"]),
  },
  methods: {
    toggleMenu() {
      const dropDown = document.querySelector("#sort-drop-down");
      dropDown.classList.toggle("hidden");
      dropDown.classList.toggle("flex");
    },
    onClickSortOption(sortType) {
      // console.log(sortType);
      this.$emit("get-sort-type", sortType);
      this.setCurrentSortType(sortType);
      this.toggleMenu();
    },
    setCurrentSortType(sortType) {
      this.currentSortType = this.sortTypes[sortType];
    },
  },
  watch: {
    filters: {
      deep: true,
      handler() {
        this.setCurrentSortType("default");
        // console.log("asdasdas");
      },
    },
  },
};
</script>