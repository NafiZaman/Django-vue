<template>
  <div class="mt-10 md:px-10 px-5">
    <div class="grid grid-cols-3">
      <div class="md:col-span-2 col-span-3 md:mr-10 items-center">
        <div class="flex rounded bg-gray-100 p-10">
          <!-- Focused Images -->
          <div class="mx-auto">
            <img
              v-if="productImages.length"
              class="
                w-100
                border
                hover:scale-150
                transition-all
                duration-500
                ease-in-out
                transform
              "
              :src="productImages[0].img"
              alt=""
            />
          </div>
        </div>
      </div>
      <div class="md:col-span-1 col-span-3">
        <!-- product name and order details -->
        <div class="flex flex-col">
          <p class="pb-2 capitalize text-xl font-bold">{{ product.name }}</p>
          <p class="py-2 capitalize text-3xl font-bold text-red-700">
            &#2547;{{ product.price }}
          </p>
          <div class="flex">
            <p class="text-sm rounded bg-gray-300 px-2 py-1 inline-flex">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M5 2a1 1 0 011 1v1h1a1 1 0 010 2H6v1a1 1 0 01-2 0V6H3a1 1 0 010-2h1V3a1 1 0 011-1zm0 10a1 1 0 011 1v1h1a1 1 0 110 2H6v1a1 1 0 11-2 0v-1H3a1 1 0 110-2h1v-1a1 1 0 011-1zM12 2a1 1 0 01.967.744L14.146 7.2 17.5 9.134a1 1 0 010 1.732l-3.354 1.935-1.18 4.455a1 1 0 01-1.933 0L9.854 12.8 6.5 10.866a1 1 0 010-1.732l3.354-1.935 1.18-4.455A1 1 0 0112 2z"
                  clip-rule="evenodd"
                />
              </svg>
              Get a &#2547;50 Reward When You Go Pro
            </p>
            <a href="#" class="ml-2 py-1 text-sm underline text-black"
              >Go Pro</a
            >
          </div>
          <div class="py-5">
            <hr />
          </div>
          <button
            @click="addToCart"
            class="
              rounded
              bg-red-700
              text-white
              py-2
              hover:bg-red-800
              font-medium
            "
          >
            Add to Cart
          </button>
          <div class="flex flex-col mt-5 rounded border-2 p-2">
            <div class="flex">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M8 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM15 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"
                />
                <path
                  d="M3 4a1 1 0 00-1 1v10a1 1 0 001 1h1.05a2.5 2.5 0 014.9 0H10a1 1 0 001-1V5a1 1 0 00-1-1H3zM14 7a1 1 0 00-1 1v6.05A2.5 2.5 0 0115.95 16H17a1 1 0 001-1v-5a1 1 0 00-.293-.707l-2-2A1 1 0 0015 7h-1z"
                />
              </svg>
              <div class="ml-2 flex flex-col">
                <div class="flex items-center">
                  <p class="font-medium flex">FREE shipping</p>
                  <p class="ml-2 text-xs text-gray-500">
                    on orders &#2547;500+
                  </p>
                </div>
                <p class="text-xs text-gray-500">Arrives in 3-7 days</p>
              </div>
            </div>
            <div class="mt-2 flex">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
                  clip-rule="evenodd"
                />
              </svg>
              <div class="ml-2 flex flex-col">
                <div class="flex items-center">
                  <p class="font-medium flex">Deliver Today</p>
                </div>
                <p class="text-xs text-gray-500">Check same day availability</p>
              </div>
            </div>
            <div class="mt-2 flex">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"
                />
              </svg>
              <div class="ml-2 flex flex-col">
                <div class="flex items-center">
                  <p class="font-medium flex">Pick up TODAY</p>
                </div>
                <p class="text-xs text-gray-500">
                  Order within 17h 33m to pick up today
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="md:col-span-1 col-span-3">
        <!-- Description -->
        <p class="pt-5 text-xl font-bold">Product Description</p>
        <p class="md:pt-5 pt-0 text-justify">
          Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ipsum
          ducimus itaque tenetur ullam dolorum, facilis assumenda asperiores
          illum sunt, eveniet porro? Itaque ipsa id corporis consectetur
          laudantium alias veritatis dolorum.
        </p>
      </div>
    </div>
    <Specifications
      :weight="product.weight"
      :brand="product.brand"
      :dimensions="product.dimensions"
      :category="product.category"
      :avg_rating="product.avg_rating"
    />
    <Reviews />
  </div>
</template>

<script>
import axios from "axios";
import Specifications from "../components/Specifications.vue";
import Reviews from "../components/Reviews.vue";

export default {
  name: "Product",
  components: {
    Specifications,
    Reviews,
  },
  data() {
    return {
      product: {},
      productImages: {},
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    addToCart() {
      if (!this.$store.state.isAuthenticated) {
        this.$router.push("/account");
      }
    },
    getProduct() {
      const productKey = this.$route.params.key;
      axios
        .get(`/api/product/get-product/${productKey}`)
        .then((response) => {
          // console.log(JSON.stringify(response.data));
          this.product = response.data;
          axios
            .get(`/api/product/get-product-images/${productKey}`)
            .then((response) => {
              // console.log(JSON.stringify(response.data));
              this.productImages = response.data;
            })
            .catch((error) => {
              console.error(error);
            });
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>