<template>
  <div>
    <div>
      <div class="flex">
        <div class="flex flex-col">
          <p class="md:text-sm text-xs text-gray-500">
            {{ resultsText }}
          </p>
          <button
            class="
              bg-gray-300
              text-black
              font-bold
              py-2
              px-4
              rounded-full
              items-center
              justify-center
              hidden
            "
            id="cls-filters"
            @click="clearFilters()"
          >
            <span>Clear Filters</span>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>

        <Sort @get-sort-type="sortProducts($event)" />
      </div>
      <div class="py-5">
        <hr />
      </div>
    </div>

    <section v-if="allProducts.length > 0 && allProducts[0].length > 0">
      <div class="all-products-grid">
        <router-link
          v-for="(p, index) in allProducts[currentPage]"
          :key="index"
          :to="{
            name: 'Product',
            params: { key: p.key, slug: p.slug },
          }"
          class="
            bg-white
            rounded
            overflow-hidden
            hover:shadow-2xl
            border-2
            hover:border-0
          "
        >
          <img class="w-full h-40 object-cover" :src="p.image" :alt="p.name" />
          <div class="p-5 pb-2">
            <p class="font-bold md:text-xl text-red-500">
              &#2547;{{ p.price }}
            </p>
            <p
              class="
                truncate
                antialiased
                capitalize
                font-medium
                hover:text-clip;
                md:text-base
                text-sm
              "
            >
              {{ p.name }}
            </p>
            <p class="pt-2 text-sm inline-flex">
              {{ p.avg_rating }} / 5
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
                />
              </svg>
            </p>
          </div>
        </router-link>
      </div>

      <div class="py-5 flex justify-center">
        <button
          class="
            rounded-full
            border-2 border-black
            mr-1
            px-2
            focus:bg-black focus:text-white
            hover:bg-black hover:text-white
          "
          v-for="index in allProducts.length"
          :key="index"
          @click="gotoProdPage(index)"
          :class="index - 1 === currentPage ? 'bg-black text-white' : ''"
        >
          {{ index }}
        </button>
      </div>
    </section>

    <section v-else>
      <img src="../assets/no_results.svg" alt="no results" class="mx-auto" />
    </section>
  </div>
</template>

<script>
import axios from "axios";
import Sort from "./Sort.vue";
// import SmallFilter from "./SmallFilter.vue";
import { mapGetters } from "vuex";

export default {
  name: "ProductsDisplay",
  components: {
    Sort,
    // SmallFilter,
  },
  data() {
    return {
      maxProdsPerPage: 12,
      currentPage: 0,
      allProducts: [],
      resultsText: "",
    };
  },
  computed: {
    ...mapGetters(["filters"]),
    resultsText() {
      var numResults = this.allProducts.reduce(
        (sum, array) => sum + array.length,
        0
      );

      if (this.currentPage === 0) {
        if (numResults > this.maxProdsPerPage)
          return `Showing 1 - ${this.maxProdsPerPage}  of ${numResults} Results`;
        else {
          return `Showing 1 - ${numResults}  of ${numResults} Results`;
        }
      } else {
        var from = this.currentPage * this.maxProdsPerPage;
        var to = (this.currentPage + 1) * this.maxProdsPerPage;
        if (to > numResults) to = numResults;
        return `Showing ${from + 1} - ${to} of ${numResults} Results`;
      }
      // return `Showing ${numResults} Results`;
      // console.log("asd");
    },
  },
  mounted() {
    this.getAllProducts();
  },
  methods: {
    sortProducts(sortType) {
      console.log("From prods disp:", sortType);
      var productsArray = this.allProducts.flat();
      if (sortType === "minMax") {
        this.setProductsPerPage(
          productsArray.sort((a, b) => (a.price > b.price ? 1 : -1))
        );
      } else if (sortType === "maxMin") {
        this.setProductsPerPage(
          productsArray.sort((a, b) => (a.price < b.price ? 1 : -1))
        );
      } else if (sortType === "alphaAsc") {
        this.setProductsPerPage(
          productsArray.sort((a, b) => (a.name > b.name ? 1 : -1))
        );
      } else if (sortType === "alphaDesc") {
        this.setProductsPerPage(
          productsArray.sort((a, b) => (a.name < b.name ? 1 : -1))
        );
      } else if (sortType === "rating") {
        this.setProductsPerPage(
          productsArray.sort((a, b) => (a.avg_rating < b.avg_rating ? 1 : -1))
        );
      }
    },
    setProductsPerPage(products) {
      const numPages = Math.trunc(products.length / this.maxProdsPerPage) + 1;
      let min = 0;
      let max = 0;
      let prodsPerPage = [];
      this.currentPage = 0;
      this.allProducts = [];

      for (let i = 0; i < numPages; i++) {
        if (i === 0) {
          min = 0;
          max = this.maxProdsPerPage;
        } else {
          min = max;
          max = (i + 1) * this.maxProdsPerPage;
        }
        if (max > products.length) max = products.length;
        // console.log(min, " - ", max);
        prodsPerPage = products.slice(min, max);
        this.allProducts.push(prodsPerPage);
      }
      // console.log(this.allProducts.length);
    },
    async getAllProducts() {
      await axios
        .get("/api/product/get-all-products")
        .then((response) => {
          this.setProductsPerPage(response.data);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    gotoProdPage(pageNum) {
      this.currentPage = pageNum - 1;
    },
    clearFilters() {
      this.$store.commit("CLEAR_FILTERS");

      var checkBoxes = document.querySelectorAll("input[type=checkbox]");
      var radioButtons = document.querySelectorAll("input[type=radio]");

      for (let i = 0; i < checkBoxes.length; i++) {
        if (checkBoxes[i].checked) checkBoxes[i].checked = false;
      }
      for (let i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) radioButtons[i].checked = false;
      }
    },
  },
  watch: {
    filters: {
      deep: true,
      async handler() {
        await axios
          .get("/api/product/get-products-by-filter", {
            params: {
              params: this.$store.state.filters,
            },
          })
          .then((response) => {
            this.setProductsPerPage(response.data);
            // console.log(response.data.length);

            const clsFilter = document.querySelector("#cls-filters");
            if (Object.keys(this.$store.state.filters).length > 0) {
              clsFilter.classList.add("inline-flex");
              clsFilter.classList.remove("hidden");
            } else {
              clsFilter.classList.add("hidden");
              clsFilter.classList.remove("inline-flex");
            }
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
  },
};
</script>