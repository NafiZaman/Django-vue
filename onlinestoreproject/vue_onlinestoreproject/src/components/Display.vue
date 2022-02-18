<template>
  <div>
    <div class="md:pl-10 pl-5">
      <p class="font-extrabold text-2xl">Products</p>
    </div>
    <div class="md:px-10 md:py-5 grid grid-cols-5">
      <div class="flex md:col-span-1 col-span-5 flex-col">
        <FilterDisplay />
        <!-- <div v-for="(items, filter) in filters" :key="filter">
          <p class="pb-2 font-bold capitalize">{{ filter }}</p>
          <div
            v-if="items.length <= 3"
            class="overflow-y-auto"
            :class="items.length * 3"
          >
            <FilterDisplay :items="items" :filterType="filter" />
          </div>
          <div v-else class="overflow-y-auto h-40">
            <FilterDisplay :items="items" :filterType="filter" />
          </div>

          <div class="py-2">
            <hr />
          </div>
        </div> -->
      </div>
      <div class="md:col-span-4 col-span-5 md:px-10 px-5">
        <ProductsDisplay />
      </div>
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import FilterDisplay from "./FilterDisplay.vue";
import ProductsDisplay from "./ProductsDisplay.vue";

export default {
  name: "Display",
  components: {
    FilterDisplay,
    ProductsDisplay,
  },
  // data() {
  //   return {
  //     filters: {},
  //   };
  // },
  // mounted() {
  //   this.getFilters();
  // },
  // methods: {
  //   getFilters() {
  //     axios
  //       .get("/api/product/get-filters")
  //       .then((response) => {
  //         for (const key in response.data) {
  //           if (Object.hasOwnProperty.call(response.data, key)) {
  //             this.filters[key] = response.data[key];
  //           }
  //         }
  //       })
  //       .catch((error) => {
  //         console.error(error);
  //       });
  //   },
  // },
};
</script>