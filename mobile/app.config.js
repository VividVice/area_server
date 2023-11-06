import 'dotenv/config';

const enableCleartextTrafficPlugin = (config) => {
  if (!config.android) config.android = {};
  if (!config.android.manifest) config.android.manifest = {};
  if (!config.android.manifest.application) config.android.manifest.application = {};

  config.android.manifest.application['android:usesCleartextTraffic'] = true;

  return config;
};

export default ({ config }) => {
  return {
    ...config,
    plugins: [
      enableCleartextTrafficPlugin,
    ],
    extra: {
      eas: {
        projectId: "71ca383b-bff6-4394-8e58-57d8e519b03c",
      },
      apikey: process.env.API_KEY_MASURAO,
      apikeychat: process.env.API_KEY_CHAT,
      apikeymeteo: process.env.API_KEY_METEO,
      apikeyblague: process.env.API_KEY_BLAGUE,
      apikeygoogle: process.env.API_KEY_GOOGLE,
      entreprise: process.env.ENTREPRISE,
    },
    owner: "lamouette",
    name: "AreaCraft",
    slug: "AreaCraft",
    version: "1.0.0",
    orientation: "portrait",
    icon: "./assets/icon.png",
    userInterfaceStyle: "light",
    splash: {
      image: "./assets/splash.png",
      resizeMode: "contain",
      backgroundColor: "#ffffff"
    },
    assetBundlePatterns: [
      "**/*"
    ],
    ios: {
      supportsTablet: true
    },
    android: {
      package: "com.company.areacraft",
      adaptiveIcon: {
        foregroundImage: "./assets/icons/logo.png",
        backgroundColor: "#ffffff"
      },
      manifest: {
        application: {
          'usesCleartextTraffic': true,
        },
        permissions: ["android.permission.INTERNET"]
      },
    },
    web: {
      favicon: "./assets/favicon.png"
    },
  };
};
