<template>
  <div>
    <div class="py-2">
      <hr />
    </div>
    <div
      class="grid md:grid-cols-4 grid-cols-2 py-5 md:px-10 px-5 pb-5 md:pb-0"
    >
      <div
        class="flex flex-col md:pb-0 mb-5"
        v-for="(items, index) in footerData"
        :key="index"
      >
        <p class="font-bold uppercase md:pb-2">{{ items.text }}</p>
        <div class="flex flex-col">
          <p
            class="capitalize md:text-sm text-xs"
            v-for="link in items.links"
            :key="link"
          >
            <a href="#" class="hover:underline">{{ link }}</a>
          </p>
        </div>
      </div>
      <!-- Social stuff -->
      <FooterSocial />
    </div>
    <div class="pb-20 text-center font-light">
      <p>Online Store Project 2022 ©</p>
    </div>
  </div>
</template>

<script>
import FooterSocial from "./FooterSocial.vue";

export default {
  name: "Footer",
  components: {
    FooterSocial,
  },
  data() {
    return {
      footerData: {
        0: {
          text: "get help",
          links: [
            "contact us",
            "frequently asked questions",
            "order status",
            "powerUp rewards credit card",
            "recall notices",
            "store feedback",
          ],
        },
        1: {
          text: "legal & privacy",
          links: [
            "privacy rights",
            "conditions of use",
            "cookie preferences",
            "do not sell my personal information",
            "privacy policy",
            "terms & conditions",
          ],
        },
        2: {
          text: "about us",
          links: [
            "accessibility",
            "affiliates",
            "careers",
            "investors",
            "suppliers",
          ],
        },
      },
    };
  },
};
</script>