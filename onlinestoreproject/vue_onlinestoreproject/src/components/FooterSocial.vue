<template>
  <div>
    <div class="flex flex-col">
      <p class="font-bold uppercase pb-1">sign up</p>
      <p class="text-xs pb-2">
        Get Exclusive Promotions, Coupons, and the Latest Events
      </p>
      <div class="flex">
        <input
          class="form-control w-full"
          type="email"
          placeholder="Enter Your E-mail"
        />
        <button
          class="text-white bg-red-700 hover:bg-red-800 rounded-r py-2 px-5"
        >
          JOIN
        </button>
      </div>
      <p class="font-bold uppercase py-2">connect with us</p>
      <p>
        <a href="#" class="hover:underline">Social</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "FooterSocial",
};
</script>