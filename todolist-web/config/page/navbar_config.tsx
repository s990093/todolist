import ChatIcon from "@mui/icons-material/Chat";
interface NavItem {
  title: string;
  url: string;
  icon: string;
  open: boolean;
}
interface NavItemTitle {
  navItems: NavItem;
}
interface PageConfig {
  navItemTitle: NavItemTitle;
  navItems: NavItem[];
}

const NavbarConfig: PageConfig = {
  navItemTitle: {
    navItems: { title: "title", url: "/", icon: "home", open: true },
  },
  navItems: [
    { title: "探索", url: "/discover", icon: "home", open: true },
    { title: "評價", url: "/post", icon: "services", open: true },
    { title: "關於", url: "/about", icon: "info", open: true },
    // { title: "回饋", url: "/feedback", icon: "info", open: true },
  ],
};

const Indexconfig = {
  title: "評價網",
  desc: "高科課程評價",
};

export default NavbarConfig;
