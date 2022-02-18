<template>
  <div>
    <div class="pt-10 md:pl-10 pl-5">
      <p class="font-extrabold text-2xl">Featured Categories</p>
    </div>
    <div class="featured-grid">
      <!-- Loop starts here -->
      <div
        class="bg-white flex flex-col items-center"
        v-for="(item, index) in featured"
        :key="index"
      >
        <a href="#" class="featured-card-inner">
          <img class="object-fill" :src="item.image" :alt="item.name" />
        </a>
        <div class="flex justify-content-center text-center">
          <a href="#" class="font-bold capitalize text-truncate">
            {{ item.name }}
          </a>
        </div>
      </div>
    </div>
    <div class="md:py-10 py-5">
      <hr />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Featured",
  data() {
    return {
      featured: [],
    };
  },
  mounted() {
    this.getFeatured();
  },
  methods: {
    getFeatured() {
      axios
        .get("/api/product/get-featured-categories")
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            this.featured.push(response.data[i]);
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>