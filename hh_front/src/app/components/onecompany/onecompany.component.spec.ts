import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OnecompanyComponent } from './onecompany.component';

describe('OnecompanyComponent', () => {
  let component: OnecompanyComponent;
  let fixture: ComponentFixture<OnecompanyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OnecompanyComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OnecompanyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
