"use client";
import {
  faHome,
  faStickyNote,
  faChartBar,
  faCog,
  faUser,
} from "@fortawesome/free-solid-svg-icons";

export const menuItems = [
  { name: "Home", href: "/", icon: faHome },
  { name: "memo", href: "/memo", icon: faStickyNote },
  { name: "Analyze", href: "analyze", icon: faChartBar },
  { name: "Settings", href: "/settings", icon: faCog },
  { name: "Friend", href: "/profile", icon: faUser },
  // { name: "Services", href: "#services", icon: faCogs },
  // { name: "Contact", href: "#contact", icon: faEnvelope },
];
