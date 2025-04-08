import { Routes } from '@angular/router';
import { CompaniesComponent } from './components/companies/companies.component';
import { OnecompanyComponent } from './components/onecompany/onecompany.component';

export const routes: Routes = [
  { path: '', redirectTo: '/companies', pathMatch: 'full' },
  { path: 'companies', component: CompaniesComponent },
  { path: 'companies/:id', component: OnecompanyComponent }
];