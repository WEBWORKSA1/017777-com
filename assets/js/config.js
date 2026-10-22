/* 017777.com site configuration.
   Payment links: paste a PayPal / Stripe Payment Link / Buy Me a Coffee / Ko-fi URL to switch
   the Support page from "pledge" mode to instant checkout. Leave blank to keep pledge mode. */
window.SITE = {
  name: "017777 Number Intelligence",
  domain: "017777.com",
  ownerContactUrl: "https://web.works/contact",
  adsenseClient: "ca-pub-6620975821265271",
  payments: {
    paypal: "",        // e.g. https://www.paypal.com/donate/?hosted_button_id=XXXX
    stripe: "",        // e.g. https://buy.stripe.com/XXXX
    buymeacoffee: "",  // e.g. https://www.buymeacoffee.com/yourname
    kofi: ""           // e.g. https://ko-fi.com/yourname
  },
  /* Form relay key (encoded, reversed base64). Never replace with a plain address. */
  _k: ["MWFza3Jvd2Jldw==", "bW9jLmxpYW1n"]
};
