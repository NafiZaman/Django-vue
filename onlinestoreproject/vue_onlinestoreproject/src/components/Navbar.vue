<template>
  <div>
    <section>
      <div class="bg-stone-800 flex md:justify-between justify-center">
        <p class="p-2 text-white text-sm font-medium ml-10">
          FREE shipping on orders over &#2547;1000
        </p>
        <div class="md:flex hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 text-white"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01"
            />
          </svg>
          <p class="p-2 text-white text-sm font-medium mr-10">Check an order</p>
        </div>
      </div>
    </section>

    <section>
      <nav class="shadow-md">
        <div class="flex justify-between p-3">
          <a href="/" class="text-3xl font-bold ml-5 text-green-900"
            ><img class="w-10" src="../assets/electron.svg" alt="site-logo"
          /></a>
          <div class="ml-10 mr-auto">
            <input
              class="
                form-control
                w-full
                mr-80
                pr-50
                py-1.5
                bg-gray-200 bg-clip-padding
                border border-solid border-gray-300
                focus:outline-none focus:shadow focus:bg-white
                md:block
                hidden
              "
              type="text"
              placeholder="Search...."
            />
          </div>
          <div class="flex">
            <a
              href="#"
              class="mr-10 text-sm hidden md:flex flex-col items-center"
            >
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
                  d="M8 7h12m0 0l-4-4m4 4l-4 4m0 6H4m0 0l4 4m-4-4l4-4"
                />
              </svg>
              <p class="hover:text-red-600">Trade-Ins</p>
            </a>
            <a
              href="#"
              class="mr-10 text-sm hidden md:flex flex-col items-center"
            >
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
                  d="M13 10V3L4 14h7v7l9-11h-7z"
                />
              </svg>
              <p class="hover:text-red-600">PowerUp Rewards</p>
            </a>
            <!-- <Account /> -->
            <router-link
              :to="{ name: 'Account' }"
              class="mr-10 text-sm flex flex-col items-center"
            >
              <svg
                v-if="!this.$store.state.isAuthenticated"
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
                  d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"
                />
              </svg>
              <svg
                v-else
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6"
                viewBox="0 0 20 20"
                fill="currentColor"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                  clip-rule="evenodd"
                />
              </svg>
              <p class="hover:text-red-600">Account</p>
            </router-link>
            <a href="#" class="mr-10 text-sm flex flex-col items-center">
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
                  d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"
                />
              </svg>
              <p class="hover:text-red-600">Cart</p>
            </a>
          </div>
        </div>
        <!-- small search -->
        <div class="px-5 pb-2 md:hidden">
          <input
            class="
              form-control
              w-full
              py-1.5
              bg-gray-200
              border border-solid border-gray-300
              focus:outline-none focus:shadow focus:bg-white
            "
            type="text"
            placeholder="Search...."
          />
        </div>
      </nav>
    </section>

    <!-- <Account /> -->

    <!-- <Login /> -->
    <!-- <div
      id="authentication-modal"
      aria-hidden="true"
      class="
        hidden
        overflow-y-auto overflow-x-hidden
        fixed
        right-0
        left-0
        top-4
        z-50
        justify-center
        items-center
        h-modal
        md:h-full md:inset-0
      "
    >
      <div class="relative px-4 w-full max-w-md h-full md:h-auto">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <div class="flex justify-end p-2">
            <button
              type="button"
              class="form-close-btn"
              data-modal-toggle="authentication-modal"
              @click="showLoginForm"
            >
              <svg
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          </div>
          <Login
            v-if="authForm === 'login'"
            @showRegistrationForm="showRegistrationForm"
          />
          <Register
            v-else-if="authForm === 'register'"
            @gotoSignin="showLoginForm"
          />
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
// import Account from "../views/Account.vue";
// import Login from "../components/Login.vue";
// import Register from "../components/Register.vue";

export default {
  name: "Navbar",
  components: {
    // Account,
    // Login,
    // Register,
  },
  // data() {
  //   return {
  //     authForm: "register",
  //   };
  // },
  // methods: {
  //   showRegistrationForm() {
  //     this.authForm = "register";
  //   },
  //   showLoginForm() {
  //     this.authForm = "register";
  //   },
  // },
};
</script>